#!/usr/bin/env pwsh

scp -i "C:\Users\User\Desktop\DevOps\Roy_key.pem" -r "C:\Users\User\Desktop\DevOps\Domain_monitoring7" ubuntu@35.85.35.156:/home/ubuntu/

ssh -i "C:\Users\User\Desktop\DevOps\Roy_key.pem" ubuntu@35.85.35.156 {
    sudo apt update
    sudo apt install -y python3-pip python3-flask
    cd Domain_monitoring7
    python3 app.py
}
