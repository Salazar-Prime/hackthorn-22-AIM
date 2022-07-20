import smtplib

def sendEmail(emailID, prediction):

    gmail_user = 'farmerhack1@gmail.com'
    gmail_password = 'aanisrfrf'

    sender = gmail_user
    receivers = [emailID]

    sent_from = gmail_user
    to = [emailID]
    subject = 'Results are Here'
    body = "The class of the uploaded image is: " + prediction

    email_text = """\
    From: %s
    To: %s
    Subject: %s

    %s
    """ % (sent_from, ", ".join(to), subject, body)
    
# try:
    smtpObj = smtplib.SMTP_SSL('smtp.gmail.com', 465)
    smtpObj.ehlo()
    smtpObj.login(gmail_user, gmail_password)
    smtpObj.sendmail(sender, receivers, body)     
    smtpObj.close()    
    print("Successfully sent email")
    # except SMTPResponseException as e:
    #     error_code = e.smtp_code
    #     error_message = e.smtp_error
    #     print(error_code)
    #     print(error_message)
