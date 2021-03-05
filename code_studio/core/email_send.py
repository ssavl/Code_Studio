import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
from config import email, password


def email_sender(name, to_email):
    msg = MIMEMultipart()

    message = f'Привет! {name}, это тестовая работа Степуры Савелия!'

    msg.attach(MIMEText(message, 'plain'))

    server = smtplib.SMTP('smtp.gmail.com: 587')
    server.starttls()
    server.login(email, password)
    server.sendmail(email, to_email, msg.as_string())
    server.quit()




