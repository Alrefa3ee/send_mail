
def send(msg):
    import smtplib
    sender_email = "alrefaeee132@gmail.com"
    rec_email = "abd516693@gmail.com"
    massage = msg
    server = smtplib.SMTP("smtp.gmail.com",587)
    server.starttls()
    server.login(sender_email,"onifdwhzgfizkwiz")
    server.sendmail(sender_email,rec_email,massage)
    server.close()