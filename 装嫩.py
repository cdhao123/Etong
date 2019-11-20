import requests
from bs4 import BeautifulSoup
url = 'http://dean.xjtu.edu.cn/'
res = requests.get(url)
html = res.text
html = html.encode('ISO-8859-1').decode('utf-8')
soup = BeautifulSoup(html,'html.parser')
titles = soup.find('ul',class_='xstz_list_ul')
titles = titles.find_all('li')
for title in titles:
    print(title.text)