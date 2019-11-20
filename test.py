import requests
from bs4 import BeautifulSoup
url = 'http://202.117.1.13/'
res = requests.get(url)
res = res.text.encode('ISO-8859-1').decode('utf-8')
print(res)