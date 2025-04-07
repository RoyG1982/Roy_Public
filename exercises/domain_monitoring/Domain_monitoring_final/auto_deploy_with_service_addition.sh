#!/bin/bash

#This script with the addition of the service, allows the flask app to run even after disconnecting from the machine
#And it starts on boot

REPO_URL="https://github.com/RoyG1982/Roy_Public.git"
APP_DIR="Roy_Public/exercises/domain_monitoring/Domain_monitoring_final"
SERVICE_NAME="flaskapp.service"
USERNAME="ubuntu"

git clone "$REPO_URL" || exit 1  // #|| =  or exit with error 1

cd "$APP_DIR" || exit 1

sudo apt update || exit 1
sudo apt install -y python3-pip || exit 1

pip3 install flask --break-system-packages || exit 1

#This creates a systemd service file at /etc/systemd/system/flaskapp.service:
#[Unit]: Defines the service description and ensures it starts after the network is up.

echo "[Unit]
Description=Flask App Deployment
After=network.target

[Service]
User=$USERNAME
WorkingDirectory=$(pwd)
ExecStart=/usr/bin/python3 app.py
Restart=always

[Install]
WantedBy=multi-user.target" | sudo tee /etc/systemd/system/"$SERVICE_NAME"

sudo systemctl daemon-reload #Reloads systemd to recognize the new service.
sudo systemctl enable "$SERVICE_NAME" #Enables the service to start on boot.
sudo systemctl start "$SERVICE_NAME" #Starts the Flask application.
sudo systemctl status "$SERVICE_NAME"
