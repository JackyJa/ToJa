import os
import time
#Install Requirements

os.system("cls")
time.sleep(0.3)
os.system("pip install --upgrade pip")
lib = ["cryptography","pyngrok","colorama","requests","json","win10toast","ctypes","getpass","smtplib"]
for i in lib:
    os.system(f"pip install {i}")
#Finish Install Requirements

import sys
from colorama import Fore
import ToJa
import banner
from cryptography.fernet import Fernet
import path
import Bomber.bomb

key2= Fernet.generate_key()

banner.banner()
banner.infolist2()

try:
    sel2 = input(Fore.LIGHTWHITE_EX+"--> ")
except KeyboardInterrupt:
    print("")
    sys.exit()

if int(sel2) == 1:
    banner.banner()
    banner.infolist1()
    try:
        sel = input(Fore.LIGHTWHITE_EX+"--> ")
    except KeyboardInterrupt:
        print("")
        sys.exit()
    if int(sel) == 1:
        ToJa.soc1()
    elif int(sel) == 2:
        ToJa.soc()
    elif int(sel) == 3:
        path.create()
    elif int(sel) == 4:
        print(Fore.RED+"\n Creator : Jacky\n"+Fore.YELLOW+" ID Telegram : @Jacky_hard\n"+Fore.GREEN+" Version : 4.0\n"+Fore.LIGHTCYAN_EX+" Channel In Telegram : @toja_github\n"+Fore.LIGHTBLUE_EX+" Please Support Us :)")
    else:
        sys.exit()

elif int(sel2) == 2:
    banner.banner()
    num = input("\n"+Fore.GREEN+" Please Enter Your Phone Number Like [0999*******] : ")
    co = input("\n"+Fore.RED+" Please Enter The Count of Round of Bombing : ")
    Bomber.bomb.bombing(phone=num,count=int(co))
    print("\n"+Fore.LIGHTMAGENTA_EX+" FINISH! ")
    time.sleep(1)
    sys.exit()


elif int(sel2) == 3:
    print(Fore.RED+"\n Creator : Jacky\n"+Fore.YELLOW+" ID Telegram : @Jacky_hard\n"+Fore.GREEN+" Version : 4.0\n"+Fore.LIGHTCYAN_EX+" Channel In Telegram : @toja_github\n"+Fore.LIGHTBLUE_EX+" Please Support Us :)")
else:
    sys.exit()