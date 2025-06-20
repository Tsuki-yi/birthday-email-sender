from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
from email.header import Header
from email.utils import formataddr
import smtplib

def send_birthday_email(to_email, to_name):
    # ✅ 使用你的 QQ 邮箱信息
    sender_email = "1824486748@qq.com"
    sender_password = "drgxrutibhkjdjij"  # 这是你从QQ邮箱获取的授权码
    smtp_server = "smtp.qq.com"
    smtp_port = 465  # ✅ QQ邮箱使用SSL端口

    from_name = "小屹的生日机器人"

    # 创建邮件对象
    msg = MIMEMultipart()
    msg['Subject'] = Header(f"生日快乐，{to_name}！", 'utf-8')
    msg['From'] = formataddr((str(Header(from_name, 'utf-8')), sender_email))
    msg['To'] = to_email

    # 邮件正文
    body = MIMEText(f"亲爱的{to_name}，祝你生日快乐！🎂🎉\n—— 来自小屹的自动祝福", 'plain', 'utf-8')
    msg.attach(body)

    try:
        with smtplib.SMTP_SSL(smtp_server, smtp_port) as server:
            server.login(sender_email, sender_password)
            server.sendmail(sender_email, to_email, msg.as_string())
        print(f"✅ 邮件已成功发送给 {to_name}")
    except Exception as e:
        if "(-1" in str(e):  # QQ邮箱常见无害报错
            print(f"⚠ 邮件已发送给 {to_name}，但捕获到非标准返回：{e}")
        else:
            print(f"❌ 发送邮件失败：{e}")