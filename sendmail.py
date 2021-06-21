def mail(to, text):
    import smtplib  
    server = smtplib.SMTP_SSL( "smtp.gmail.com", 465 )
    server.login( "absarqureshi55@gmail.com", "passwd@1234" )
    server.sendmail( "absarqureshi55@gmail.com", to, text )
    server.quit()

