import re
import os
import copy
print(os.path.abspath(__file__))
print(os.path.dirname(__file__))

with open(f"{os.path.dirname(__file__)}\phone.txt") as of:
    reads=of.read()
    #print(read) 

tel=[]
tel1=[]

shablon= re.compile(r"380\d\d\d\d\d\d\d\d\d")
shablon1= re.compile(r"\d\d\d?\d\d\d\d\d\d\d\d\d")
shablon2= re.compile(r"(\d\d)(\d\d\d)(\d\d\d)(\d\d)(\d\d)")    #разбивает на группы
shablon3= re.compile(r"""
\+?3?8?
\(?|\s?|-?
\d{3}
\)?|\s?|-?
\d
\)?|\(?|\s?|-?
\d
\)?|\(?|\s?|-?
\d
\)?|\(?|\s?|-?
\d
\)?|\(?|\s?|-?
\d
\)?|\(?|\s?|-?
\d
\)?|\(?|\s?|-?
\d""", re.VERBOSE)
shablon4= re.compile(r"""3
8
0
\d
\d
\d
\d
\d
\d
\d
\d
-?
\d""", re.VERBOSE)


tel= re.findall(shablon, reads)
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

tel_groyp= re.findall(shablon2,reads)
print(tel_groyp)

tel_ne_obyaz= re.findall(shablon1,reads)
print(tel_ne_obyaz)

tt= re.findall(shablon4,reads)
print(tt)