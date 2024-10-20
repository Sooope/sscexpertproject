import json
import requests

url = "https://aos.ssc.edu.hk/aos/e-sportsday/student/index.php"
payload = {"input_unique_id": "a", "input_pass": "a", "btn_login": "Submit"}
prox = {'https': "socks5://127.0.0.1:9050"}
r = requests.get(url, params=payload, proxies=prox)
print(str(r.content))




