#!/bin/bash

# Define the location of your private key and local path
PRIVATE_KEY="/mnt/c/Users/User/Desktop/DevOps/Roy_key.pem"  # Update to WSL/Windows format if using Git Bash or WSL
LOCAL_PATH="/mnt/c/Users/User/Desktop/DevOps/Domain_monitoring7"  # Path in WSL/WSL

# Copy the Domain_monitoring7 folder to the AWS instance
scp -i "$PRIVATE_KEY" -r "$LOCAL_PATH" ubuntu@35.85.35.156:/home/ubuntu/

# SSH into the AWS instance
ssh -i "$PRIVATE_KEY" ubuntu@35.85.35.156 << EOF

# Update the system and install required packages
sudo apt update
sudo apt install -y python3-pip python3-flask

# Navigate to the project folder
cd /home/ubuntu/Domain_monitoring7

# Run the application
python3 app.py

EOF
