import smtplib,time,schedule
from email.mime.text import MIMEText
from email.header import Header
#引入smtplib、MIMETex和Header
QQ1 = input('请输入你的QQ号：')
password = input('请输入你的授权码：')
QQ2 = input('请输入你要发送给QQ：')
inside = input('请输入邮件内容：')
title = input('请输入邮件主题：')
spot = input('请输入你想发送邮件的时间(格式示例08:05)：')
def job(QQ1,password,QQ2,inside,title,spot):
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

schedule.every().day.at(spot).do(job,QQ1,password,QQ2,inside,title,spot)
while True:
    schedule.run_pending()
    time.sleep(1)
