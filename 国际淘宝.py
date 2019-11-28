from bs4 import BeautifulSoup
from selenium import webdriver
import requests
import time
url = 'https://world.taobao.com/'
driver = webdriver.Chrome()
driver.get(url)
time.sleep(1)
page_Source = driver.page_source
html = BeautifulSoup(page_Source,'html.parser')
html = html.find('div',class_="zebra-oversea-feeds-pc")
html = html.find('div',class_="content")
pictures = html.find_all('div',class_="img-wraper")
urls = []
for picture in pictures:
    picture = picture.find('img')
    sr = 'https:' + str(picture)[30:-3]
    urls.append(sr)
count = 1
driver.close()
for url in urls:
    res = requests.get(url).content
    File_name = str(count) + '.jpg'
    File = open(File_name,'wb')
    File.write(res)
    File.close()
    count += 1

