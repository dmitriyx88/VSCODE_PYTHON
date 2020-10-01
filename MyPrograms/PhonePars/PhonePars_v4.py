import re
import os
import copy
#print(os.path.abspath(__file__))
#print(os.path.dirname(__file__))

with open(f"{os.path.dirname(__file__)}\phone.txt") as of:
    reads=of.readlines()
    #print(reads[1216]) 

shablon= re.compile(r"380\d\d\d\d\d\d\d\d\d", re.DOTALL)
shablon1= re.compile(r"\d\d\d?\d\d\d\d\d\d\d\d\d")
shablon2= re.compile(r"(\d\d)(\d\d\d)(\d\d\d)(\d\d)(\d\d)")    #разбивает на группы
shablon3= re.compile(r"""
(\+38(\)|\(|\s|-)?|38(\)|\(|\s|-)?)?
(\d){3}
(\)|\(|\s|-)?
\d
(\)|\(|\s|-)?
\d
(\)|\(|\s|-)?
\d
(\)|\(|\s|-)?
\d
(\)|\(|\s|-)?
\d
(\)|\(|\s|-)?
\d
(\)|\(|\s|-)?
\d""", re.VERBOSE|re.DOTALL)

newList=[]

i=0

while i<len(reads):
    result= re.search(shablon3,reads[i])
    
    if result is None:
        i=i+1
        continue
    
    print(result)
    st= result.start()
    en= result.end()
   
    newList.append(reads[i][st:en])
    i=i+1
    

print(newList)