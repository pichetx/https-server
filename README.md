# https-server
https-server for Termux ( Node.js )
-----------------------------------------------

* แตะหน้าจอค้าง แล้วเลือก more ไปติีก keep screen on
```
termux-setup-storage
```
* กดยอมรับ
```
pkg update -y
```
* (ใส่ค่า n ในทุกการเรียกถาม)

```
pkg install git -y
```

```
cd storage/downloads
```
```
git clone https://github.com/pichetx/https-server
```
```
cd https-server
```

```
chmod +x install.sh
```
```
sh install.sh
```
หลังจากเปิดไฟล์ bash.bashrc กด enter เลื่อนเคอร์เซอร์ขึ้นบรรทัดแรกเพิ่ม

```
run-node
```
กด ctrl+x แล้วตอบ y เพื่อ save

การใช้งาน
ctrl c เพื่อหยุด
edit-miner เพื่อแก้ไข pool,wallet.pass
run-node เพื่อ run server
--------------------------------
# การใช้งานรูปแบบอื่น
-ใช้เป็นที่เก็บไฟล์ สำหรับdownload ภายในเครือข่ายเดียวกัน โดยนำไฟล์ที่ต้องการใช้งานไปเก็บไว้ในแฟ้มdownload เช่นไฟล์ชื่อ lotto
  การdownload โดยใช้ browser เช่น chrome google ทำได้โดย พิมพ์ http://(ipและportตามหน้าnode.js)
จะเข้าสู้หน้าindex เลือกdownloads ตามต้องการ
  การdownload โดยใช้ termux ให้cd ไปยังpathที่จะใช้save พิมพ์ wget http://(ipและportตามหน้าnode.js)/lotto
  สามารถใช้download ได้เฉพาะไฟบ์เท่านั้น หากรูปแบบเป็นfolderจะไม่สามารถdownloadได้