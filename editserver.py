import os, time, json




def banner():
	os.system("clear")
 print("\033[1;34;40m")
	os.system("figlet -f big VERUS")
	os.system("figlet -f digital http-server")
 print("\033[36m\033[0m")   print("\033[36mEdit by PICHET SAENGTEWAN\033[0m")
	print("\033[36m\033[0m")

def setminer():


    banner()
    try:
        print("ตัวอย่าง: \033[93mstratum+tcp://ap.luckpool.net:3956\033[00m")
        print("        \033[93mstratum+tcp://verus.asia.mine.zergpool.com:3300\033[00m")
        pool = input(" pool : ")
        print("\033[35m-----------------------------------------\033[0m")
        

        print("ตัวอย่าง: \033[93mRQpWNdNZ4LQ5yHUM3VAVuhUmMMiMuGLUhT\033[00m")
        wallet = input("wallet: ")
        print("\033[35m-----------------------------------------\033[0m")
        

        print("ตัวอย่าง: \033[93mx หรือ ( hybrid เฉพาะ luckpool )\033[00m")
        print("        \033[93mc=DOGE,mc=VRSC ไม่ต้องใส่ id=ชื่อ ระบบจะ add auto\033[00m")
        password = input("password : ")
        print("\033[35m-----------------------------------------\033[0m")
        
        if pool == "" or wallet == "":
            raise Exception()
        if password == "":
            password = "x"
    except:
        os.system("@cls||clear")
        print("เกิดข้อผิดพลาดโปรดตั้งค่าใหม่!")
        time.sleep(3)
        os.system("python3 editserver.py")

    push = {
        'pool': pool,
        'wallet': wallet,
        'pass': password
    }
    with open("online.json", "w") as set:
        json.dump(push, set, indent=4)


while True:
    banner()
    setminer()
    break
