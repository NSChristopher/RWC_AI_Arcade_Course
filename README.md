# AI_Pygame_Playground


# Setup Codespaces Desktop Lite and Connect Through the Web Browser

## Instructions

### Step 1: Update `devcontainer.json`

Add the `desktop-lite` feature and forward the necessary ports by
adding the following lines to the devcontainer.json file (don't remove the
image parameter already in the file):

```json
{
  "features": {
    "ghcr.io/devcontainers/features/desktop-lite:1": {}
  },
  "forwardPorts": [6080, 5901],
  "portsAttributes": {
    "6080": {
      "label": "noVNC"
    },
    "5901": {
      "label": "VNC"
    }
  },
  "runArgs": ["--shm-size=1g"]
}
```

### Step 2: Rebuild the Codespace

- Open the command palette in VS Code (`F1` or `Ctrl+Shift+P`).
- Select `Remote-Containers: Rebuild Container`.

### Step 3: Set Up the VNC Server

1. **Install TigerVNC:**

    ```sh
    sudo apt-get update
    sudo apt-get install -y tigervnc-standalone-server
    ```

2. **Set a VNC password:**

    ```sh
    vncpasswd
    ```

3. **Start the VNC server:**

    ```sh
    vncserver :1 -geometry 1280x800 -depth 24
    ```

### Step 4: Start the noVNC Service

1. **Install noVNC and websockify:**

    ```sh
    sudo apt-get install -y novnc websockify
    ```

2. **Start the noVNC service:**

    ```sh
    websockify --web=/usr/share/novnc/ 6080 localhost:5901
    ```

### Step 5: Forward Ports in VS Code

- Open the command palette in VS Code (`F1` or `Ctrl+Shift+P`).
- Select `Ports: Focus on Ports View` to bring the Ports view into focus.
- Ensure that ports `6080` and `5901` are forwarded.

### Step 6: Connect Using a Browser

1. Open the Ports view in VS Code.
2. Locate the port labeled `noVNC` (6080).
3. Click the Globe icon to open the noVNC web client in your browser.
4. Click the `Connect` button and enter the VNC password.

## Example Commands Recap

1. **Install dependencies:**

    ```sh
    sudo apt-get update
    sudo apt-get install -y tigervnc-standalone-server novnc websockify
    ```

2. **Set VNC password:**

    ```sh
    vncpasswd
    ```

3. **Start VNC server:**

    ```sh
    vncserver :1 -geometry 1280x800 -depth 24
    ```

4. **Start noVNC service:**

    ```sh
    websockify --web=/usr/share/novnc/ 6080 localhost:5901 &
    ```

5. **Stop both services**

    ```sh
    pkill -f websockify
    ```

    ```sh
    ps aux | grep websockify
    # Identify the PID (process ID) from the output, then run:
    kill <PID>
    ```
  

By following these steps, you should be able to set up and connect to a lightweight desktop environment in GitHub Codespaces using TigerVNC and noVNC.
