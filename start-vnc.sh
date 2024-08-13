#!/bin/bash

# Start the VNC server without a password
echo "Starting VNC server without password"
vncserver :1 -geometry 1280x800 -depth 24 -SecurityTypes None

# Start the noVNC service
echo "Starting noVNC service"
websockify --web=/usr/share/novnc/ 6080 localhost:5901 &
