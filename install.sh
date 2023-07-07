#!/bin/sh

apt-get update -y
apt-get upgrade -y

chmod +x run-node

mv run-node /data/data/com.termux/files/usr/bin

cd /data/data/com.termux/files/usr/bin

chmod +x run-node

cd && cd /data/data/com.termux/files/usr/etc
nano bash.bashrc

