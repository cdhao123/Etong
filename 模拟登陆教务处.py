import requests,time
import smtplib
from selenium import webdriver
from email.mime.text import MIMEText
from email.header import Header
from selenium.webdriver.chrome.options import Options
def job(inside,QQ1 = '2248662312',password = 'pbarajfxibpidiej' ,QQ2 = '2248662312',title = '空闲教室'):
    mailhost='smtp.qq.com'
    #把qq邮箱的服务器地址赋值到变量mailhost上，地址应为字符串格式
    qqmail = smtplib.SMTP()
    #实例化一个smtplib模块里的SMTP类的对象，这样就可以调用SMTP对象的方法和属性了
    qqmail.connect(mailhost,25)
    #连接服务器，第一个参数是服务器地址，第二个参数是SMTP端口号。
    #以上，皆为连接服务器。

    account = QQ1+'@qq.com'
    #获取邮箱账号，为字符串格式
    password = password
    #获取邮箱密码，为字符串格式
    qqmail.login(account,password)
    #登录邮箱，第一个参数为邮箱账号，第二个参数为邮箱密码
    #以上，皆为登录邮箱。

    receiver=QQ2+'@qq.com'
    #获取收件人的邮箱。

    content= inside
    #输入你的邮件正文，为字符串格式
    message = MIMEText(content, 'plain', 'utf-8')
    #实例化一个MIMEText邮件对象，该对象需要写进三个参数，分别是邮件正文，文本格式和编码
    subject = title
    #输入你的邮件主题，为字符串格式
    message['Subject'] = Header(subject, 'utf-8')
    #在等号的右边是实例化了一个Header邮件头对象，该对象需要写入两个参数，分别是邮件主题和编码，然后赋值给等号左边的变量message['Subject']。
    #以上，为填写主题和正文。

    try:
        qqmail.sendmail(account, receiver, message.as_string())
        print ('邮件发送成功')
    except:
        print ('邮件发送失败')
    qqmail.quit()
    key = input('按任意键退出，输入continue明日同一时间继续发送！')
    if key == 'continue':
        pass
    else:
        exit()
driver = webdriver.Chrome()
url = 'http://ehall.xjtu.edu.cn/new/index.html'
driver.get(url)
# button_1 = driver.find_element_by_xpath(r'/html/body/div[4]/div[1]/div[3]/div[4]/table/tbody/tr[1]/td/a/img')
# button_1.click()
# time.sleep(2)
# print(driver.page_source)
time.sleep(2)
button_2 = driver.find_element_by_id("ampHasNoLogin")
button_2.click()
time.sleep(2)
user_name = driver.find_element_by_xpath(r'//*[@id="form1"]/input[1]')
user_name.send_keys('2193612793')
pass_word = driver.find_element_by_xpath(r'//*[@id="form1"]/input[2]')
pass_word.send_keys('CHEN159753')
button_3 = driver.find_element_by_xpath(r'//*[@id="account_login"]')
button_3.click()
time.sleep(2)
url = 'http://ehall.xjtu.edu.cn/jwapp/sys/kxjas/*default/index.do?amp_sec_version_=1&gid_=dWF4OTJlMTBvZGh0MGVpVTU4bXZNd1pqTVZPM3E4Z3R5ZlBxRCtLbTl6UWpta0ViK0lRN0Y5Y0M5Q3JBa3dndUpEeGpMNWNyU2tNRllydWlwaGk2OEE9PQ&EMAP_LANG=zh&THEME=cherry#/kxjscx'
driver.get(url)
url = 'http://ehall.xjtu.edu.cn/jwapp/sys/kxjas/modules/kxjscx/cxkxjs.do'
driver.get(url)
cookies = driver.get_cookies()
driver.close()
cookie = [item["name"] + "=" + item["value"] for item in cookies]
cookiestr = ';'.join(item for item in cookie)
headers = {
    'Cookie': cookiestr,
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/78.0.3904.97 Safari/537.36'
}
room_code = input('请输入要查询的教室代码，多个用逗号隔开（范围1001~*）：')
start = input('请输入开始节次：')
end = input('请输入结束节次：')
timeday = time.strftime("%Y-%m-%d %H:%M:%S", time.localtime())[:10]
datas = {
    'KXRQ': timeday,
    'JXLDM': room_code,
    'JSJC': start,
    'KSJC': end
}
res = requests.post(url,headers = headers,data = datas).json()
rooms = res['datas']['cxkxjs']['rows']
roomlist = ''
for room in rooms :#room为列表
    roomlist = roomlist + room['JASMC']+'\n'
job(roomlist)