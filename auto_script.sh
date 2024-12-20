#!/bin/bash
scp -i "/c/Users/User/Desktop/DevOps/Roy_key.pem" -r "/c/Users/User/Desktop/DevOps/Domain_monitoring7" ubuntu@35.85.35.156:/home/ubuntu/
ssh ubuntu@35.85.35.156 -i /c/Users/User/Desktop/DevOps/Roy_key.pem
sudo apt update
sudo apt install python3-pip
sudo apt install python3-flask
cd Domain_monitoring7
python3 app.py
