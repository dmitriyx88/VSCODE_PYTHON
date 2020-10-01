rim = [("I",1),("V",5),("X",10),("L",50),("C",100),("D",500),("M",1000)]
inp_text = input("Введите римское чило: ")

def find_rim(c):
    for x,y in rim:
        if c==x: break 
    return y


inp_list =[]
for v in inp_text:
    b = find_rim(v)
    inp_list.append(b)
print(inp_list)

cnt=(len(inp_list))-1
sum=0
i=0
b=0
while i<=cnt:
    if i>0: 
        b=i-1
    if i==0 and sum==0:
        sum=inp_list[i]
        print("1:",sum, " i=  ",i)
        i=i+1
        continue
    
    if inp_list[i]>inp_list[b]:
        
        print("2:",sum, " i=  ",i)
        sum= (sum - inp_list[b]) + (inp_list[i]-inp_list[b])
    

    if inp_list[i]<=inp_list[b]:
        sum= sum + (inp_list[i])
        print("3:",sum, " i=  ",i)
 
    
    i=i+1




print(sum)











