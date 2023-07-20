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
