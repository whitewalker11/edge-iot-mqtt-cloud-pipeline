
#!/bin/bash
sudo apt update
sudo apt install -y mosquitto mosquitto-clients python3-pip
pip3 install -r edge/requirements.txt
