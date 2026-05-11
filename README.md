<div align="center">
  <h1>ShopAssist</h1>

  <sub>Formerly Autonomous Shopper Assistance System<sub>
  
  <p>
    ShopAssist is an 
    <a href="https://en.wikipedia.org/wiki/Automated_convenience_store">
      Autonomous Shopper Assistance System
    </a> 
    which aims to provide an effortless shopping experience to customers in retail environments.
    Disguised as a shopping cart, it navigates autonomously to lead the user to their desired products or follow them around, removing the physical hassle of handling a cart.
  </p>
  <br>

[![Python](https://img.shields.io/badge/Python-3776AB?logo=python&logoColor=fff)](https://www.python.org/)
[![ROS2](https://img.shields.io/badge/ROS2-%2339457E.svg?logo=ros&logoColor=fff)](https://ros.org/)
[![LangChain](https://img.shields.io/badge/LangChain-1c3c3c.svg?logo=langchain&logoColor=fff)](https://www.langchain.com/)
[![FastAPI](https://img.shields.io/badge/FastAPI-009688?logo=fastapi&logoColor=fff)](https://fastapi.tiangolo.com/)
[![MongoDB](https://img.shields.io/badge/MongoDB-%234ea94b.svg?logo=mongodb&logoColor=fff)](https://www.mongodb.com/)
[![ReactJS](https://img.shields.io/badge/ReactJS-%2320232a.svg?logo=react&logoColor=fff)](https://react.dev/)
[![Docker](https://img.shields.io/badge/Docker-2496ED?logo=docker&logoColor=fff)](https://www.docker.com/)
[![Podman](https://img.shields.io/badge/Podman-%2339457E?logo=podman&logoColor=fff)](https://podman.io/)

<br>
</div>

---

> [!WARNING]
> The copyright of this project is held by a corporate.<br>
> Kindly read the [LICENSE](https://github.com/muditmehta07/asas#license) before cloning or copying this project.

## Showcase
<div align="center">
  <img src=".assets/IMG_dash.png" width="100%" alt="Showcase Top">
  <div style="display: flex; justify-content: space-between; margin-top: 10px;">
    <img src=".assets/IMG_gazebo.png" width="49%" alt="Showcase Bottom Left">
    <img src=".assets/IMG_rviz.png" width="49%" alt="Showcase Bottom Right">
  </div>
</div>


## Folders

```text
├── backend          # fastapi server
├── frontend         # react dashboard
├── ros_ws           # ros2 workspace
├── rack_model       # rack model (duh)
├── mongo-seed       # database
└── docker-compose.yml
```

## Installation

- **Linux** or **macOS** (via Docker or Podman)
- `xhost` installed (optional, for GUI forwarding)

1. **Clone the repo:**
   ```bash
   git clone https://github.com/muditmehta07/asas.git
   cd asas
   ```

2. **Allow Docker/Podman to access X server:**
   ```bash
   xhost +local:docker
   ```
   or
   ```bash
   xhost +local:podman
   ```

4. **Launch:**

   **Using Docker:**
   ```bash
   sudo docker compose -f docker-compose.yml up --build
   ```

   **Using Podman:**
   ```bash
   podman-compose -f compose.yaml up --build
   ```
5. **Open dashboard at** http://localhost:5173
   
## Contributing

Anyone can contribute to this project, just send a PR.

> [!IMPORTANT]
> While submitting a Pull Request, please add an `[ai]` flag to your commit message if your contribution contains AI code. This helps maintain transparency.


## License

This project is developed and maintained by [muditmehta07](https://github.com/sponsors/muditmehta07/)

Licensed under the **GNU Affero General Public License v3.0 (AGPL-3.0)**. Read fill [LICENSE](https://github.com/muditmehta07/asas/blob/main/LICENSE)
> [!WARNING]
> Under the terms of the AGPL-3.0, any modifications or use of this software in a network service must be made available under the same license. For commercial licensing, proprietary integrations, or partnerships, please contact the firm's technical department.

Copyright © 2026 FOUR M Education and Technology Private Limited.
