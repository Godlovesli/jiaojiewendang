#coding=utf-8
import yagmail
from conf import setting

def sendmail(title,content,attrs=None):
    m = yagmail.SMTP(host=setting.MAIL_HOST,
                 user = setting.MAIL_USER,
                 password=setting.MAIL_PASSWRD,
                 smtp_ssl=True
                 )
    m.send(to = setting.TO,subject=title,
           contents = content,
           attachments = attrs)
    print('发送邮件完成')

