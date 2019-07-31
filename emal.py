
import smtplib
 
HOST = "smtp.i.ua"
SUBJECT = "Test email from Python"
TO = "ts.dp@i.ua"
FROM = "python@mydomain.com"
text = "Python 3.4 rules them all! kuku"
 
BODY = "\r\n".join((
    "From: %s" % FROM,
    "To: %s" % TO,
    "Subject: %s" % SUBJECT ,
    "",
    text
))
 
server = smtplib.SMTP(HOST)
server.sendmail(FROM, [TO], BODY)
server.quit()