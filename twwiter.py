from selenium import webdriver
from bs4 import BeautifulSoup
import time
from selenium.webdriver.chrome.options import Options
from wordcloud import WordCloud
url = 'https://twitter.com/realDonaldTrump'
chromedriver_path="C:\\Program Files\\Python37\\chromedriver.exe"#驱动链接
options = webdriver.ChromeOptions()
# 此步骤很重要，设置为开发者模式，防止被各大网站识别出来使用了Selenium
options.add_experimental_option('excludeSwitches', ['enable-automation']) 
driver = webdriver.Chrome(executable_path=chromedriver_path, options=options)
driver.get(url)
js="var q=document.documentElement.scrollTop="
for i in range(100):
    driver.execute_script(js+str(10000*(i+1)))
    time.sleep(0.5)
page_source = driver.page_source
html = BeautifulSoup(page_source,'html.parser')
tweets = html.find_all('div',class_="content")
text =''
for tweet in tweets:
    try:
        time = tweet.find('small',class_="time")
        time = time.find_all('span')[0].text
        tweet = tweet.find('p')
        print(time)
        print(tweet.text.strip())
        text += tweet.text.strip()
        print('-----------------------------------------------')
    except:
        pass
wordcloud = WordCloud(scale=16,background_color='white').generate(text)
image_produce = wordcloud.to_image()
image_produce.show()
driver.close()
