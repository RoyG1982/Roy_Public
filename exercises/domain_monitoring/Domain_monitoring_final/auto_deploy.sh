#!/bin/bash

KEY_PATH="/mnt/c/Users/User/Desktop/AWS_key/RoyG_key.pem"
USER="ubuntu"
HOST="35.89.235.135"
REPO_URL="https://github.com/RoyG1982/Roy_Public.git"
APP_DIR="Roy_Public/exercises/domain_monitoring/Domain_monitoring_final"

# SSH into the AWS instance and execute commands
ssh -i "$KEY_PATH" -t $USER@$HOST << "EOF"
    set -e  # Exit on any error

    echo "Updating system packages..."
    echo "<password>" | sudo -S apt update

    echo "Installing Python and pip..."
    echo "<password>" | sudo -S apt install -y python3-pip

    echo "Cloning the repository..."
    git clone "$REPO_URL" || (cd Roy_Public && git pull)

    cd "$APP_DIR"

    echo "Installing Flask..."
    pip3 install flask --break-system-packages

    echo "Starting Flask app..."
    python3 app.py
EOF
