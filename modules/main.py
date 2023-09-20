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

key2= Fernet.generate_key()

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
    print(Fore.GREEN+"\n [*] "+Fore.WHITE+"Please Wait For Building Exe File... \n")
    time.sleep(1)
    ToJa.soc3()
elif int(sel) == 4:
    print(Fore.RED+" Creator : Jacky\n"+Fore.YELLOW+" ID Telegram : @Jacky_hard\n"+Fore.GREEN+" Version : 2.0\n"+Fore.LIGHTCYAN_EX+" Channel In Telegram : @toja_github\n"+Fore.LIGHTBLUE_EX+" Please Support Us :)")
else:
    sys.exit()