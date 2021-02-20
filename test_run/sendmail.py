#邮件配置
import smtplib
from email.mime.text import MIMEText
from email.header import Header
from email.mime.multipart import MIMEMultipart


def sendmail(sender,password,receiver,file_path,file_name):
    smtpserver = 'smtp.qq.com'
    msg = MIMEMultipart()
    mail_subject='菜小秘自动化测试邮件'
    msg['Subject'] = Header(mail_subject,'utf-8')
    msg['From'] = sender
    msg['to'] = ','.join(receiver)#此处是设置发送给多人邮件的关键
    #邮件正文
    msg.attach(MIMEText('请下载附件并使用浏览器打开附件文件', 'plain', 'utf-8',))

    #附件内容
    att1= MIMEText(open(file_path,'rb').read(),'base64','utf-8')
    att1['Content-Type'] = 'application/octet-stream'
    att1['Content-Disposition'] = 'attachment; filename="%s"'%file_name
    msg.attach(att1)
    try:
        smtp = smtplib.SMTP()
        smtp.connect(smtpserver)
        smtp.login(sender,password)
        smtp.sendmail(sender,receiver,msg.as_string())
        smtp.quit()
        print("邮件发送成功")
    except smtplib.SMTPException:
        print("发送失败")
