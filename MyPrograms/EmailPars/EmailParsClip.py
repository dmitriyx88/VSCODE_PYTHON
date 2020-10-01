import pyperclip
import re

emails=[]
c= pyperclip.paste()

mail_shablon= re.compile(r"[a-zA-Z0-9_.-]+@[a-zA-Z0-9_.]+\.[a-z]{2,6}" )

res=re.findall(mail_shablon, c)
if len(res) == 0:
    print("В буфере обмена не содержится текст включающий Email")
print(res)


