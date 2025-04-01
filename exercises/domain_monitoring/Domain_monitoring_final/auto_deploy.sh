#!/bin/bash

git clone https://github.com/RoyG1982/Roy_Public.git
sudo apt update
sudo apt install python3-pip -y
pip3 install flask --break-system-packages
cd Roy_Public/exercises/domain_monitoring/Domain_monitoring_finalls
python3 app.py