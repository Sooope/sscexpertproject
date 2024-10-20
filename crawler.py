import json
import requests

url = "https://api.ipify.org?format=json"
prox = {'https': "socks5://127.0.0.1:9050"}
r = requests.get(url, proxies=prox)
print(r.json())




