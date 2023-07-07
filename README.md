# https-server
https-server for Termux ( Node.js )

termux-setup-storage

pkg update

pkg install git -y && pkg install nano

cd storage/downloads

git clone https://github.com/pichetx/htts-server

cd https-server

chmod +x install.sh

sh install.sh

หลังจากเปิดไฟล์ bash.bashrc เพิ่มบรรทัดแรกเป็น

run-node
