# Use the base Codespace image
FROM mcr.microsoft.com/devcontainers/universal:2

# Install necessary packages
RUN apt-get update && apt-get install -y \
    tigervnc-standalone-server \
    novnc \
    websockify \
    swig

# connect to existing venv
RUN echo "source venv/bin/activate" >> ~/.bashrc
