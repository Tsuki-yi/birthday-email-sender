import csv
from datetime import datetime

# 读取生日数据
with open("/Users/renyi/python-learn/birhday_wisher.csv", encoding="utf-8") as file:
    reader = csv.DictReader(file)
    birthdays = list(reader)

# 获取今天日期
today = datetime.today().strftime("%m-%d")

# 检查今天是否有人过生日
for person in birthdays:
    if person["birthday"] == today:
        print(f"🎉 今天是 {person['name']} 的生日！祝他/她生日快乐！🎂")
from email_sender import send_birthday_email


# 检查今天是否有人过生日
for person in birthdays:
    if person["birthday"] == today:
        print(f"🎉 今天是 {person['name']} 的生日！准备发送邮件…")
        send_birthday_email(person["email"], person["name"])