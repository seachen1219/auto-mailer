import smtplib
from email.message import EmailMessage

# 請把這兩行換成你自己的 Gmail 資訊
EMAIL = "shihyi.chen1219@gmail.com"
PASSWORD = "pczi zbxp qfmt mdfy"

def send_email():
    to = input("To（F44114049@gs.ncku.edu.tw）: ")
    subject = input("Subject（test）: ")
    content = input("Message（這封信是用python寄的喔!!!）: ")

    msg = EmailMessage()
    msg["Subject"] = subject
    msg["From"] = EMAIL
    msg["To"] = to
    msg.set_content(content)

    try:
        with smtplib.SMTP_SSL("smtp.gmail.com", 465) as smtp:
            smtp.login(EMAIL, PASSWORD)
            smtp.send_message(msg)
            print("✅ Email 寄出成功！")

    except Exception as e:
        print(f"❌ 寄信失敗：{e}")

if __name__ == "__main__":
    send_email()
