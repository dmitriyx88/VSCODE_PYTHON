import re
import os
import copy
print(os.path.abspath(__file__))
print(os.path.dirname(__file__))

with open(f"{os.path.dirname(__file__)}\phone.txt") as of:
    reads=of.read()
    #print(read) 

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
shablon4= re.compile(r"""
[\+380(-]*
0 
[-\s)(]*
\d
[-\s)(]*
\d
[-\s)(]*
\d
[-\s)(]*
\d
[-\s)(]*
\d
[-\s)(]*
\d
[-\s)(]*
\d
[-\s)(]*
\d
[-\s)(]*
\d""", re.VERBOSE)



tt= re.findall(shablon4,reads)
print(tt)