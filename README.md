# https-server
https-server for Termux ( Node.js )
-----------------------------------------------

termux-setup-storage

pkg update -y

pkg install git -y && pkg install nano

cd storage/downloads

git clone https://github.com/pichetx/https-server

cd https-server

mv run-node /data/data/com.termux/files/usr/bin

cd /data/data/com.termux/files/usr/bin

chmod +x run-node

cd && cd ../etc

nano bash.bashrc

หลังจากเปิดไฟล์ bash.bashrc เพิ่มบรรทัดแรกเป็น

run-node
