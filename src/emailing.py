import smtplib

def sendEmail(emailID, prediction):

    gmail_user = 'farmerhack1@gmail.com'
    gmail_password = 'aanisrfrf'

    sender = gmail_user
    receivers = [emailID]

    message = """
    Subject: Results for image upload are here:

    Classification is %s
    """%(receivers[0])
    sent_from = 'goat@ngoyo.com'
    to = [emailID]
    subject = 'Results are Here'
    body = "The class of the uploaded image is: " + prediction

    email_text = """\
    From: %s
    To: %s
    Subject: %s

    %s
    """ % (sent_from, ", ".join(to), subject, body)
    
    try:
        smtpObj = smtplib.SMTP_SSL('smtp.gmail.com', 465)
        smtpObj.ehlo()
        smtpObj.login(gmail_user, gmail_password)
        smtpObj.sendmail(sender, receivers, message)     
        smtpObj.close()    
        print("Successfully sent email")
    except smtplib.SMTPException:
        print("Error: unable to send email")
