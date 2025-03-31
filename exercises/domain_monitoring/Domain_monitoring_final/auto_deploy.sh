#!/bin/bash

git clone https://github.com/RoyG1982/Roy_Public.git
cd /Roy_Public/exercises/domain_monitoring/Domain_monitoring_final
sudo apt update
sudo apt install python3-pip
pip3 install flask --break-system-packages