import smtplib

smtp_obj= smtplib.SMTP_SSL("smtp.ukr.net", 465)
print(smtp_obj.ehlo())
print(smtp_obj.login("st_amator@ukr.net", "EKt1Cv62zt82FToW"))

FROM="st_amator@ukr.net"
TO="dmitriyx@bk.ru"
SUBJECT="Hello Dmitro!!!"
text="Where do your live?"

BODY = "\r\n".join((
    "From: %s" % FROM,
    "To: %s" % TO,
    "Subject: %s" % SUBJECT ,
    "",
    text
))

print(BODY)
print(smtp_obj.sendmail("st_amator@ukr.net", "dmitriyx@bk.ru", BODY))