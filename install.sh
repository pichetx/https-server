#!/bin/sh

apt-get update -y
apt-get upgrade -y
apt install python3 -y
apt install figlet -y
apt install nodejs -y
npm install http-server -g

chmod +x run-node
chmod +x edit-miner

mv run-node /data/data/com.termux/files/usr/bin
mv edit-miner /data/data/com.termux/files/usr/bin

cd /data/data/com.termux/files/usr/bin

chmod +x run-node
chmod +x edit-miner

cd && cd /data/data/com.termux/files/usr/etc
nano bash.bashrc

