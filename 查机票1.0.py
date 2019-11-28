import requests,time
from urllib.request import quote
from bs4 import BeautifulSoup
from urllib.request import quote
from selenium import webdriver
from selenium.webdriver.chrome.options import Options

print('------------------欢迎使用机票查询系统----------------------')
time.sleep(1)
headers = {
    'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/76.0.3809.132 Safari/537.3'
}

#查机场三字码
def getcode(url):
    res = requests.get(url,headers = headers).text
    soup = BeautifulSoup(res,'html.parser')
    soup = soup.find_all('tr')[2]
    code = soup.find_all('td')[1].text.strip()
    code = code.lower()
    print('机场代码为：'+code)
    return code
chrome_option = Options()
chrome_option.add_argument('--headless')
airport_from = input('请输入您的出发地：')
# airport_from = '西安'
airport_from_utf = airport_from.encode('utf-8')
url = 'https://airportcode.51240.com/'+ quote(airport_from_utf) +'__airportcodesou/'
airport_from_code = getcode(url)
airport_to = input('请输入您的目的地：')
# airport_to = '哈尔滨'
airport_to_utf = airport_to.encode('utf-8')
url = 'https://airportcode.51240.com/'+ quote(airport_to_utf) +'__airportcodesou/'
airport_to_code = getcode(url)

#查询机票
data = input('请输入索要查询的日期（格式例如2019-09-30):')
# data = '2020-01-10'
def job(data):
    data_store = int(data[-2:])
    #print(data_store)
    url = 'https://flights.ctrip.com/itinerary/oneway/'+airport_from_code+'-'+airport_to_code+'?date='+data
    driver = webdriver.Chrome(options=chrome_option)
    driver.get(url)
    print('正在查询，请耐心等待四秒...')
    time.sleep(4)
    html = driver.page_source
    soup = BeautifulSoup(html , 'html.parser')
    Flights = soup.find_all('div',class_="search_box search_box_tag search_box_light Label_Flight")
    print('查询日期为%s'%data)
    print('航班号               出发地          出发时间       经停            目的地         到达时间        票价')
    for Flight in Flights:
        name = Flight.find(class_="logo-item flight_logo").text[:10]
        preplace = Flight.find(class_="inb right")
        delay = Flight.find(class_="inb center").text
        destination = Flight.find(class_="inb left")
        start_time = preplace.find(class_="time").text
        preplace = preplace.find(class_="airport").text
        arrive_time = destination.find(class_="time").text
        destination = destination.find(class_="airport").text
        price = Flight.find('span',class_="base_price02").text
        delay_len = 10-(len(delay) - 4)*2
        space = ''
        for i in range(delay_len):
            space += ' '
        if(delay == ''):
            print(name+'       '+preplace+'    '+start_time+'        '+'直达  '+'        '+destination+'     '+arrive_time+'        '+price)
        else:
            print(name+'       '+preplace+'    '+start_time+'        '+delay[2:]+space+destination+'     '+arrive_time+'        '+price)
    driver.close()
    key = input('输入exit退出，输入b查看前一天的航班信息，输入a查看后一天航班信息')
    return key,data_store
while True:
    res = job(data)
    if res[0] == 'exit':
        break
    elif res[0] == 'b':
        day = res[1] -1
        data = data[:-2]+str(day)
    else:
        day = res[1] +1
        data = data[:-2]+str(day)
# print(data)

