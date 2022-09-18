
# 发送
```python
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
from email.mime.image import MIMEImage
import smtplib



# 配置邮箱及密码
from_mail = 'frommail@163.com'
from_mail_password = 'passwd'
to_mail = '2594398228@qq.com'



# 设置总的邮件体对象，对象类型为mixed
msg = MIMEMultipart('mixed')

# 邮件的发件人及收件人信息
msg['From'] = from_mail
msg['To'] = to_mail

# 邮件的主题
msg['Subject'] = 'python mail test'


# 构造文本内容
text_info = 'hello world'
text_sub = MIMEText(text_info, 'plain', 'utf-8')
msg.attach(text_sub)


# 构造超文本
url = "https://blog.csdn.net/u010520724"
html_info = """
<p>点击以下链接，你会去向一个更大的世界</p>
<p><a href="%s">click me</a></p>
<p>i am very galsses for you</p>
"""% url
html_sub = MIMEText(html_info, 'html', 'utf-8')
# 如果不加下边这行代码的话，上边的文本是不会正常显示的，会把超文本的内容当做文本显示
html_sub["Content-Disposition"] = 'attachment; filename="csdn.html"'
# 把构造的内容写到邮件体中
msg.attach(html_sub)


# 构造图片
image_file = open(r'E:\python\python.jpg', 'rb').read()
image = MIMEImage(image_file)
image.add_header('Content-ID', '<image1>')
# 如果不加下边这行代码的话，会在收件方方面显示乱码的bin文件，下载之后也不能正常打开,这个地方也可以对文件重命名
image["Content-Disposition"] = 'attachment; filename="red_people.png"'
msg.attach(image)

# 构造附件
txt_file = open(r'E:\python\test2.py', 'rb').read()
txt = MIMEText(txt_file, 'base64', 'utf-8')
txt["Content-Type"] = 'application/octet-stream'
#以下代码可以重命名附件为hello_world.txt
txt.add_header('Content-Disposition', 'attachment', filename='test.py')
msg.attach(txt)


try:
    server = smtplib.SMTP('smtp.163.com')
    server.docmd('ehol', from_mail)
    server.starttls()
    server.login(from_mail,from_mail_password)

    server.sendmail(from_mail,to_mail,msg.as_string())
    server.quit()
    print('sendemail successful!')
except Exception as e:
    print('sendemail failed next is the reason')
    print(e)

```



```python
import imaplib
import email


email_service = "outlook.office365.com"
# email_service_port = 993
email_user = "tom-nonobody@outlook.com"
email_passwd = "1111"


get_mail_server = imaplib.IMAP4_SSL(email_service)
get_mail_server.login(email_user, email_passwd)

# #各种操作
get_mail_server.select("Inbox")  # 邮件数量与占用空间
mail_type, mail_date = get_mail_server.search(None, "UNSEEN", '(FROM "liu2946181970@126.com")')  # 第一个选项为none则全部展示 'ALL",  "SEEN"

fetch_data_list = []
for num in mail_date[0].split():
    typ, fetch_data = get_mail_server.fetch(num, '(RFC822)')
    fetch_data_list.append(fetch_data)


# 得到【第一封邮件】【】【主要部分】
msg = email.message_from_bytes(fetch_data_list[0][0][-1])

msg["Subject"]
msg['Date']
msg['from']


for part in msg.walk():
    print(part.get_content_type)  # 查看邮件的所有类型
    if part.get_content_maintype == 'text':
        body = part.get_payload(decode=True)
        text = body.decode('utf-8')  # 对text部分进行解码
    if part.get_content_maintype == "image":
        filename = part.get_filename()
        content = part.get_payload(decode=True)
        with open(filename, "wb") as f:
            f.write(content)
```

