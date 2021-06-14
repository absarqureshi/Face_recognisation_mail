def mail(to, text):
    import smtplib  
    server = smtplib.SMTP_SSL( "smtp.gmail.com", 465 )
    server.login( "sheikh.69-cse-1@mietjammu.in", "passwd@11921345211" )
    server.sendmail( "sheikh.69-cse-1@mietjammu.in", to, text )
    server.quit()

