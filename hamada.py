import requests


domain = input("\033[91m[+] Enter the Domain :: ")
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
        print("\033[92m[+]Discovered Subdomain "+url)