years = int(input("Введите значение года:"))
import calendar 

def leapyears(y):
    x = calendar.isleap(y)   
    return x

m = leapyears(years) 
if m: n=f"Да действительно {years} год высокосный"
else: n=f"Нет {years} год не высокосный"


print(n)