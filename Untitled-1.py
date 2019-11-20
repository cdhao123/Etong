import requests
from bs4 import BeautifulSoup
phone = input('输入你的手机号：')
url = 'https://org.xjtu.edu.cn/openplatform/g/admin/sendVeriCodeLogin'
headers = {
    'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/78.0.3904.97 Safari/537.36'
}
datas={
    'optionType': "login",
    'templeType': "smscode",
    'username': '13576084875',
    'veriType': "sms"
}
res = requests.post(url,headers=headers,data=datas).json()
print(res)
token = res['validate_token']
code = input('请输入验证码：')
url = 'https://h5.ele.me/restapi/eus/login/login_by_mobile'
datas = {
    'mobile': phone,
    'scf': "ms",
    'validate_code': code,
    'validate_token': token
}
res = requests.post(url,headers=headers,data=datas)
print(res.text)