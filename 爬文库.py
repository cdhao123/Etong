import time
from bs4 import BeautifulSoup
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
copy = ''
url = input('请输入链接')
chromedriver_path="C:\\Program Files\\Python37\\chromedriver.exe"#驱动链接
options = webdriver.ChromeOptions()
# 此步骤很重要，设置为开发者模式，防止被各大网站识别出来使用了Selenium
options.add_experimental_option('excludeSwitches', ['enable-automation']) 
driver = webdriver.Chrome(executable_path=chromedriver_path, options=options)
options = webdriver.ChromeOptions()
driver.get(url)
# driver.maximize_window()
time.sleep(2)
page_source = driver.page_source
html = BeautifulSoup(page_source,'html.parser')
pages = int(html.find('span',class_="page-count").text[1:])
try:
    button = driver.find_element_by_css_selector("[class='moreBtn goBtn']")
    driver.execute_script("arguments[0].scrollIntoView();", button)
    button.click()
    time.sleep(1)
except:
    pass
height = 1047
top = 650
if pages <= 50:
    for i in range(1,pages+2):
        try:
            js="var q=document.documentElement.scrollTop="+str(top)
            top += height
            driver.execute_script(js)
            time.sleep(1.5)
            page_source = driver.page_source
            html = BeautifulSoup(page_source,'html.parser')
            content = html.find_all('div',class_="reader-txt-layer")
            if (i+1)%3 == 0:
                for word in content:
                    print(word.text) 
                time.sleep(0.5)
        except:
            pass
else:
    for i in range(0, 51 ):
        try:
            js="var q=document.documentElement.scrollTop="+str(top)
            top += height
            driver.execute_script(js)
            time.sleep(1)
            page_source = driver.page_source
            html = BeautifulSoup(page_source,'html.parser')
            content = html.find_all('div',class_="reader-txt-layer")
            for word in content:
                print(word.text)
            time.sleep(0.5)
        except:
            driver.close()
    driver.get(url+'?pn=51')
    # button = driver.find_element_by_css_selector("[class='pageList-btn next-pageList hidden-doc-banner']")
    # # driver.execute_script("arguments[0].scrollIntoView();", button)
    # button.click()
    time.sleep(1)
    pages = pages - 50
    height = 1047
    top = 450
    for i in range(2, pages+2):
        try:
            js="var q=document.documentElement.scrollTop="+str(top)
            top += height
            driver.execute_script(js)
            time.sleep(0.5)
            page_source = driver.page_source
            html = BeautifulSoup(page_source,'html.parser')
            content = html.find_all('div',class_="reader-txt-layer")
            for word in content:
                print(word.text)
            time.sleep(0.5)
        except:
            driver.close()
print('抓取完成')
driver.close()
key = input('按任意键结束')
exit

