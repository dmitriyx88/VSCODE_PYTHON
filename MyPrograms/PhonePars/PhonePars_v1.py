import os
print(os.getcwd())
numb=[]
with open(r"MyPrograms/PhonePars/olx.txt", mode="r") as of:
    rfile= of.read()
    #print(rfile)
    of.close()

if str('data-phone="') in rfile:
    print("True")
    vhozgdenie=0
    for i in range(0, rfile.count('data-phone=')):
        vhozgdenie= rfile.find('data-phone="',vhozgdenie)+12
        #print(vhozgdenie)
        numb.append(rfile[vhozgdenie:vhozgdenie+13])
        #print(rfile[vhozgdenie:vhozgdenie+13])
    
print(numb)