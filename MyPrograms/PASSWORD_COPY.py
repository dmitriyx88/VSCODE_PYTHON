import pyperclip
import sys
import getpass

pin=False
PASS={"dm":"PASSWORD_Dima", "pb":"PASSWORD_Artem", "am":"PASSWORD_Mama"}

for i in range(1, len(sys.argv)):
    ar=str(sys.argv[i])
    if i==1 and getpass.getpass("PIN:") == str(1744): 
        pin=True
        print("PIN-Ok")
    if i==1 and pin==True:
        ar=ar[1:]
        if ar in PASS:
            pyperclip.copy(PASS[ar])
            print(ar, "-Ok")
        else:
            print("Аргумент не известен")


# Выполнять с командной строки

