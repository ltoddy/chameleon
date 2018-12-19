import smtplib
import email.utils
from email.mime.text import MIMEText

from config import HOST, PORT

msg = MIMEText('Just for test 测试邮件内容')
msg['To'] = email.utils.formataddr(('Sender', 'tester@example.com'))
msg['From'] = email.utils.formataddr(('Receiver', 'ltoddy@example.com'))
msg['Subject'] = 'test 标题'

server = smtplib.SMTP(HOST, PORT)
try:
    server.sendmail('tester@example.com', ['ltoddy@example.com'], msg.as_string())
finally:
    server.quit()
