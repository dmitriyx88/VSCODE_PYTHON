import os
import re

file_open= open(f"{os.path.dirname(__file__)}\phone.txt", "r", encoding="utf-8")
file= file_open.read()
file_open.close()

file_list= file.split("\n")

for i in range(len(file_list)):
    file_list[i]=file_list[i].split("\t")

    y=0
    while y<len(file_list[i]):
        if y == len(file_list[i]):
            break
        if file_list[i][y]=="":
            del file_list[i][y]
        else:
            y=y+1

print(file_list)


phone_list=[]


shablon_= re.compile(r"380\d\d\d\d\d\d\d\d")
shablon1= re.compile(r"380\d\d\d\d\d\d\d\d")
shablon_= re.compile(r'''
[+]?[3]?[()\s-]?[8]?[()\s-]?0[()\s-]?\d[()\s-]?\d[()\s-]?\d[()\s-]?\d[()\s-]?\d[()\s-]?\d[()\s-]?\d[()\s-]{0,1}\d
''', re.VERBOSE|re.DOTALL)

for i in range(len(file_list)):
    for y in range(len(file_list[i])):
        result3 = re.search(shablon1, file_list[i][y])
        result1 = re.findall(shablon_, file_list[i][y])
        #result2 = re.match(shablon1, file_list[i][y])
        print(result3)
        for n in range(len(result1)):
            if len(result1[n])>0:
                phone_list.append(result1[n])

        
        
        
        
        
        





print(len(file_list))
print(phone_list, len(phone_list))