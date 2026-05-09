# Autonomous Shopper Assistance System

> [!WARNING]
> Kindly do not copy this project, read the [LICENSE](https://github.com/muditmehta07/asas/edit/main/LICENSE) first.

A system that navigates the shopper to the desired item using an autonomous shopping cart in a simulated environment.

## Installation

> [!TIP]
> The containerized setup only works on `Linux` and `Mac`, pls configure it yourself on that bloated `Windows`.

Run the following `Docker` commands in the cloned folder:
```bash
xhost +local:docker

sudo docker compose -f docker-compose.yaml up --build
```
OR, in case you prefer `Podman`

```bash
xhost +local:podman

podman-compose -f compose.yaml up --build
```
  
## Contributing

Anyone can contribute to this project, just send a PR.

> [!IMPORTANT]
> Add an `[ai]` flag to your commit message to convey that your work contains AI-generated code.
