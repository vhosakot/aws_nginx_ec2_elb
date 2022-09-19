#!/bin/bash

sudo apt-get -y update
sudo apt-get -y upgrade
sudo apt-get -y install nginx
sudo systemctl status nginx
sudo echo "<!DOCTYPE html><html><body><h1>Cisco SPL</h1></body></html>" > /var/www/html/index.nginx-debian.html
sudo systemctl restart nginx
