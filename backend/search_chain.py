import os
import re
import numpy as np
from pymongo import MongoClient
from dotenv import load_dotenv
from langchain_ollama import OllamaEmbeddings

load_dotenv()

MONGO_URI = os.getenv("MONGO_URI", "mongodb://localhost:27017")
DB_NAME   = "supermarket_sim"

embeddings_model = OllamaEmbeddings(
    model="nomic-embed-text", 
    base_url="http://127.0.0.1:11434"
)

_client = MongoClient(MONGO_URI)
_inv_col = _client[DB_NAME]["rack_inventory"]
_racks_col = _client[DB_NAME]["racks"]

def cosine_similarity(v1, v2):
    v1, v2 = np.array(v1), np.array(v2)
    return np.dot(v1, v2) / (np.linalg.norm(v1) * np.linalg.norm(v2))

def sync_embeddings():
    print("[AI Startup] Syncing embeddings...")
    for doc in _inv_col.find({}):
        updated_items = []
        for item in doc.get("items", []):
            text = f"product: {item['name']}, category: {item.get('category', '')}"
            item["embedding"] = embeddings_model.embed_query(text)
            updated_items.append(item)
        _inv_col.update_one({"_id": doc["_id"]}, {"$set": {"items": updated_items}})
    print("[AI Startup] Done.")

def _build_response(item, rack_id, query):
    rack_doc = _racks_col.find_one({"rack_id": rack_id}, {"_id": 0, "dock_point": 1})
    dock = rack_doc.get("dock_point") if rack_doc else None
    return {
        "found": True, "query": query, "item_name": item["name"],
        "rack_id": rack_id, "category": item.get("category", ""),
        "price": item.get("price", 0.0), "stock": item.get("stock", 0),
        "dock_point": dock, "message": f"Found **{item['name']}** on **{rack_id}**."
    }

def search_item(query: str) -> dict:
    query_clean = query.strip().lower()
    if not query_clean: return {"found": False, "message": "Empty query."}

    search_words = [w for w in re.split(r'\s+', query_clean) if len(w) > 3 or w == "milk"]
    
    for word in search_words:
        regex_match = _inv_col.find_one(
            {"items.name": {"$regex": word, "$options": "i"}},
            {"rack_id": 1, "items.$": 1}
        )
        if regex_match:
            return _build_response(regex_match["items"][0], regex_match["rack_id"], query)

    try:
        query_vector = embeddings_model.embed_query(query_clean)
        best_match, highest_score = None, -1.0
        
        for rack in _inv_col.find({"items.embedding": {"$exists": True}}):
            for item in rack.get("items", []):
                if "embedding" in item:
                    score = cosine_similarity(query_vector, item["embedding"])
                    if score > highest_score:
                        highest_score, best_match = score, {"item": item, "rack_id": rack["rack_id"]}

        if best_match and highest_score > 0.5: # Strict threshold
            return _build_response(best_match["item"], best_match["rack_id"], query)
    except: pass

    return {"found": False, "query": query, "message": f"Could not find '{query}'."}

def get_nearest_rack(x, y, max_dist=2.0):
    racks = list(_racks_col.find({}))
    nearest, min_d = None, max_dist
    for r in racks:
        dp = r.get("dock_point")
        if not dp: continue
        dist = ((dp["x"] - x)**2 + (dp["y"] - y)**2)**0.5
        if dist < min_d: min_d, nearest = dist, r
    return nearest

def get_rack_items(rack_id):
    doc = _inv_col.find_one({"rack_id": rack_id})
    return doc.get("items", []) if doc else []

def get_all_inventory():
    inventory_map = {d["rack_id"]: d.get("items", []) for d in _inv_col.find({})}
    racks = list(_racks_col.find({}).sort("rack_id", 1))
    return [{"rack_id": r["rack_id"], "group": r.get("group", ""), "items": inventory_map.get(r["rack_id"], [])} for r in racks]

try:
    if not _inv_col.find_one({"items.embedding": {"$exists": True}}):
        sync_embeddings()
except: pass