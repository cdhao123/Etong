save =''
text = '''Accept: text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3
Accept-Encoding: gzip, deflate
Accept-Language: zh-CN,zh;q=0.9,en;q=0.8
Cache-Control: max-age=0
Connection: keep-alive
Content-Length: 36
Content-Type: application/x-www-form-urlencoded
Cookie: JSESSIONID=8D43502C29F1E2C6C7BA41771B818217
Host: pj.xjtu.edu.cn
Origin: http://pj.xjtu.edu.cn
Referer: http://pj.xjtu.edu.cn/teavote/front/index.do?method=showteacher&id=33
Upgrade-Insecure-Requests: 1
User-Agent: Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/78.0.3904.108 Safari/537.36'''
for word in text:
    if word == ':':
        word = "':'"
    elif word == '\n':
        word =  "',\n'"
    elif word  == ' ':
        word =''
    else:
        word = word
    save += word
print("'%s'"%save)
