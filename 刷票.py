import requests
from bs4 import BeautifulSoup
url = 'http://pj.xjtu.edu.cn/teavote/cas/vote.do?method=ad&type=t1&tid=33'
datas = {
    'pj': 'a',
    'imageField.x': '87',
    'imageField.y': '15'
}
headers = {
    'Accept':'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3',
    'Accept-Encoding':'gzip,deflate',
    'Accept-Language':'zh-CN,zh;q=0.9,en;q=0.8',
    'Cache-Control':'max-age=0',
    'Connection':'keep-alive',
    'Content-Length':'36',
    'Content-Type':'application/x-www-form-urlencoded',
    'Cookie':'JSESSIONID=74F3080ED0B0F554953CCA0263D71F18',
    'Host':'pj.xjtu.edu.cn',
    'Origin':'http://pj.xjtu.edu.cn',
    'Referer':'http://pj.xjtu.edu.cn/teavote/front/index.do?method=showteacher&id=33',
    'Upgrade-Insecure-Requests':'1',
    'User-Agent':'Mozilla/5.0(WindowsNT10.0;Win64;x64)AppleWebKit/537.36(KHTML,likeGecko)Chrome/78.0.3904.108Safari/537.36'
}
res = requests.post(url,data=datas,headers=headers)
print(res.text)