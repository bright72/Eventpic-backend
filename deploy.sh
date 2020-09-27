#!/bin/bash
sudo yum update
sudo yum install epel-release

sudo cd /var/www/html
sudo git clone https://github.com/bright72/Eventpic-backend.git

sudo cd Eventpic-backend/
sudo git pull
sudo npm install
sudo npm install pm2@latest -g
sudo pm2 stop eventpic-backend
sudo pm2 start eventpic-backend.js
sudo systemctl restart nginx