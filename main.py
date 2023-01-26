import socket
import requests
import os
import json


f = """\033[95m
____  ____      _____ ___   ___  _     ____
/ ___||  _ \    |_   _/ _ \ / _ \| |   / ___|
\___ \| | | |_____| || | | | | | | |   \___ 
 ___) | |_| |_____| || |_| | |_| | |___ ___) |
|____/|____/      |_| \___/ \___/|_____|____/

\033[93mAuther : \033[94mMohamed Sulieman
\033[93mGitHub : https://github.com/hamadax2
Facebook : https://www.facebook.com/king.hamada.sd
"""
p = '''\033[94mHow do you want to continue
\033[97m[1]-Enter the url  manually
[2]-Import a text file
[+]-print Exit or Stop to Exit
'''
m = """
THE MENU 
[1] Change host to ip tool
[2] Subdomain Finder
[3] IP Info                                 
"""
os.system("clear")
print(f)
print(m)
chose1 = int(input("Please Chose One Option :: "))
if chose1 == 2:
    str = """\033[93m
    ____        _     ____    _____ _           _
    / ___| _   _| |__ |  _ \  |  ___(_)_ __   __| | ___ _ __
    \___ \| | | | '_ \| | | | | |_  | | '_ \ / _` |/ _ \ '__|
     ___) | |_| | |_) | |_| | |  _| | | | | | (_| |  __/ |
    |____/ \__,_|_.__/|____/  |_|   |_|_| |_|\__,_|\___|_|
    """
    os.system("clear")
    print(str)
    domain = input("\033[94m[+] Enter the Domain :: ")
    file = open("raw.txt")
    content = file.read()
    subdomains = content.splitlines()
    for subdomain in subdomains:
        url = f'https://{subdomain}.{domain}'
        try:
            requests.get(url)
            print(url)
        except:
            pass
        else:
            print("\033[92m[+] Discovered Subdomain " + url)
            with open("url", "w") as file:
                file.write(url)
elif chose1 == 1:
    print(p)
    chose = int(input())
    if chose == 1:
        os.system("clear")
        while True:
            try:
                url = input("\033[94mPlease Enter The Url : ")
                if url.lower() == "exit" or url.lower() == "stop":
                    break
                host = socket.gethostbyname(url)
                print(url+" : "+host)
            except :
                print("Error Check Your Host or Internet connection ")
    elif chose == 2:
        os.system("clear")
        print("\033[91mNote !!, You have to move the text file to the script folder \n")
        inline = open(input("Please Enter The file name : "))
        line = inline.readline()
        line = line.strip()
        url = line
        ip = socket.gethostbyname(url)
        print(line+" : "+ip)
        while line != "":
            line = inline.readline()
            line = line.strip()
            ip1 = socket.gethostbyname(url)
            print(line+" : " + ip1)
            if line == "":
                print("Done")
elif chose1 == 3:
    ipinfo = """\033[91m
 ____  _ _         ___        __       
/ ___|(_) |_ ___  |_ _|_ __  / _| ___  
\___ \| | __/ _ \  | || '_ \| |_ / _ \ 
 ___) | | ||  __/  | || | | |  _| (_) |
|____/|_|\__\___| |___|_| |_|_|  \___/ 
                                      
    """
    os.system("clear")
    print(ipinfo)
    try:
        ip = input("Enter The Site URL :: ")
        req = requests.get("https://"+ip)
        print("\n"+str(req.headers))
        gethostby = socket.gethostbyname(ip)
        print("\nThe IP Adress Of "+ip+" Is "+gethostby)
    #ip info
        req2 = requests.get("https://ipinfo.io/"+gethostby+"/json")
        response = json.loads(req2.text)
        print("Location : "+response["loc"])
        print("Region : "+ response["region"])
        print("City : "+response["city"])
        print("Country : "+response["country"])
    except requests.exceptions.ConnectionError :
        print("\033[91mError Check Your Internet Connection !")
