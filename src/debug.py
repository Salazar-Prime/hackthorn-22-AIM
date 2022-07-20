import smtplib

try:
    server = smtplib.SMTP('smtp.gmail.com', 485)
    server.ehlo()
except:
    print('Something went wrong...')