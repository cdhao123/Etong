import time
import requests
from bs4 import BeautifulSoup
time_accurate = str(time.time())
time_stamp = time_accurate[:10] + time_accurate[11:14]
url = 'https://org.xjtu.edu.cn/openplatform/g/admin/getIsShowJcaptchaCode?userName=2193612793&_=' + time_stamp
headers = {
    'Accept':'*/*',
    'Accept-Encoding':'gzip,deflate,br',
    'Accept-Language':'zh-CN,zh;q=0.9,en;q=0.8',
    'Connection':'keep-alive',
    'Content-Type':'application/x-www-form-urlencoded',
    'Cookie':'route=7ee49a7421c3f563a7b57a532bfd53bb;JSESSIONID=833783B8C68C4BA53AAC37913B94F38F;cur_appId_=Wh+FE117l+4=;state=xjdCas;sid_code=workbench_login_jcaptcha_833783B8C68C4BA53AAC37913B94F38F;memberId=804421;usertypekey=1;employeenokey=2193612793;CASTGC=TGT-358543-rmEXj6W5qttt0bbLMYWUJlgyIBq96IezRZ3AdzD3xPBC4dbeRg-gdscas01;open_Platform_User=user_token_cec398a5-a4a7-4b5e-a071-d6cb3fbfc6d9',    
    'Host':'org.xjtu.edu.cn',
    'Referer':'https://org.xjtu.edu.cn/openplatform/login.html',
    'Sec-Fetch-Mode':'cors',
    'Sec-Fetch-Site':'same-origin',
    'User-Agent':'Mozilla/5.0(WindowsNT10.0;Win64;x64)AppleWebKit/537.36(KHTML,likeGecko)Chrome/78.0.3904.97Safari/537.36'
}
params = {
    'userName': '2193612793',
    '_': time_stamp
}
res = requests.get(url,headers=headers,params=params)
print(res.text)
url = 'https://org.xjtu.edu.cn/openplatform/g/admin/login'
headers = {
    'Accept': '*/*',
    'Accept-Encoding': 'gzip, deflate, br',
    'Accept-Language': 'zh-CN,zh;q=0.9,en;q=0.8',
    'Connection': 'keep-alive',
    'Content-Length': '90',
    'Content-Type': 'application/json;charset=UTF-8',
    'Cookie': 'route=a3bd3ffc3d7852ff2de7c604a51733cd; JSESSIONID=99CDA34A500AD9584E548C60062B4805; app_info_urla=+L4rB7r6yuXaNSyCPpJbv37GCbbuXhbEZ/qFiels81u38P4uqqTgoCG6/OeB13xANyc3U/KciIkaUIyMOZj+nSzforMLmGm9sIsTr4XffJQo3GI/5/EaWaxqg2NwOKqc3DXU57Q4WDOKCJuZGP5+0NviIPnbljsP/YFKqt8rYxSqiOUrK26kUKUhhaCtsiRE; cur_appId_=Wh+FE117l+4=; state=xjdCas; sid_code=workbench_login_jcaptcha_99CDA34A500AD9584E548C60062B4805',
    'Host': 'org.xjtu.edu.cn',
    'Origin': 'https://org.xjtu.edu.cn',
    'Referer': 'https://org.xjtu.edu.cn/openplatform/login.html',
    'Sec-Fetch-Mode': 'cors',
    'Sec-Fetch-Site': 'same-origin',
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/78.0.3904.97 Safari/537.36'
}
datas = {
    'jcaptchaCode': "",
    'loginType': "1",
    'pwd': "UvXPqXMjo8AQEXLnavLOpw==",
    'username': "2193612793"
}
res = requests.post(url,headers=headers,data=datas)
print(res.text)
