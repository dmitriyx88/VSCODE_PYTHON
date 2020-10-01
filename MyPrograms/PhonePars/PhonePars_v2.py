import re
import os
print(os.path.abspath(__file__))
print(os.path.dirname(__file__))

with open(f"{os.path.dirname(__file__)}\phone.txt") as of:
    read=of.read()
    #print(read) 

tel=[]
tel1=[]

shablon= re.compile(r"380\d\d\d\d\d\d\d\d\d")
shablon1= re.compile(r"\d\d\d\d\d\d\d\d\d\d\d\d")
shablon2= re.compile(r"(\d\d)(\d\d\d)(\d\d\d)(\d\d)(\d\d)")    #разбивает на группы

tel= re.findall(shablon, read)
print(tel)
print("Теперь уберем 38")
tel2=[]
for i in range(0, len(tel)):
    if tel[i][0:3]=="380": 
        #tel2.append(tel[i][2:])
        tel[i]=tel[i][2:]
        tel2.append("+38("+tel[i][0:3]+")"+tel[i][3:6]+"-"+tel[i][6:8]+"-"+tel[i][8:])

print(tel)
print("-------------------")
print(tel2)

tel_groyp= re.findall(shablon2,read)
print(tel_groyp)