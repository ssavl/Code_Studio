import smtplib
from code_studio.config import email, password


# smtpObj = smtplib.SMTP('smtp.gmail.com', 587)
#
# smtpObj.starttls()
#
# smtpObj.login(email, password')
#
# smtpObj.sendmail('blooomed@gmail.com', "get-moscow@yandex.ru", "fuck you!")
#
# smtpObj.quit()
#
# import smtplib


def send_email(subject, to_addr, from_addr, body_text):
    """
    Send an email
    """

    BODY = "\r\n".join((
        "From: %s" % from_addr,
        "To: %s" % to_addr,
        "Subject: %s" % subject,
        "",
        body_text
    ))

    server = smtplib.SMTP('smtp.gmail.com', 587)
    server.sendmail(from_addr, [to_addr], BODY)
    server.quit()


if __name__ == "__main__":
    # host = "mySMTP.server.com"
    subject = "Test email from Python"
    to_addr = "get-moscow@yandex.ru"
    from_addr = email
    body_text = "Python rules them all!"
    send_email(subject="Test email from Python", to_addr="get-moscow@yandex.ru", from_addr=email,
               body_text="Python rules them all!")
