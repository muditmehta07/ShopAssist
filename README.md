# Autonomous Shopper Assistance System

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
|
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

### Getting Started

1. **Clone the repo:**
   ```bash
   git clone https://github.com/muditmehta07/asas.git
   cd asas
   ```

2. **Allow Docker to access X server:**
   ```bash
   xhost +local:docker
   ```

3. **Launch:**

   **Using Docker:**
   ```bash
   sudo docker compose -f docker-compose.yml up --build
   ```

   **Using Podman:**
   ```bash
   xhost +local:podman
   podman-compose -f compose.yaml up --build
   ```

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
