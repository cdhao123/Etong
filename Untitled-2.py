import requests 
import chardet
from bs4 import BeautifulSoup
url = 'https://www.woaidu.net/book_65724.html'
res = requests.get(url)
html= res.text
html = html.encode('ISO-8859-1').decode('utf-8')
soup=BeautifulSoup(html,'html.parser')
titles=soup.find('ul',class_="dataList")
titles=titles.find_all('li')
for title in titles :
    print(title)