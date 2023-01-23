import requests
import os
str = """\033[93m
____        _     ____    _____ _           _
/ ___| _   _| |__ |  _ \  |  ___(_)_ __   __| | ___ _ __
\___ \| | | | '_ \| | | | | |_  | | '_ \ / _` |/ _ \ '__|
 ___) | |_| | |_) | |_| | |  _| | | | | | (_| |  __/ |
 |____/ \__,_|_.__/|____/  |_|   |_|_| |_|\__,_|\___|_|
 
 Auther : \033[94mMohamed Sulieman
 \033[93mGitHub : https://github.com/hamadax2
 Facebook : https://www.facebook.com/king.hamada.sd
 
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
                        except requests.ConnectionError:
                                    pass
                                else:
                                            print("\033[92m[+] Discovered Subdomain "+url)
