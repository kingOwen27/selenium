import smtplib
from email.mime.text import MIMEText
from email.header import Header

# 发送邮件标题
subject = 'Python email test'

# 编写HTML类型的邮件正文
msg = MIMEText('<html><h1>你好！</h1></html>', 'html', 'utf-8')
msg['Subject'] = Header(subject, 'utf-8')

# 连接发送邮件
smtp = smtplib.SMTP()
smtp.connect("smtp.126.com")
smtp.login("w1209574292@126.com", "FJTSPUPVTENGFSPG")
smtp.sendmail("w1209574292@126.com", "1209574292@qq.com", msg.as_string())
smtp.quit()
