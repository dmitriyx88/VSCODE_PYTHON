regim = input("Режим: 1- Если хотите узнать является ли нужное число простым \n      любая клвиша- если хотите найти все простые числа от 1 до Х:  ")
if regim==1: x = input("Введите число: ")
if regim!=1: x = input("Выберите период от 0 до :")

if x.isnumeric(): x=float(x)
else:
    while x.isnumeric()==False:
        x = input("Введите корректное число: ")
x=float(x)


def prostoe(c):
    i=c
    spisok=[]
    while i>0:
        if c%i==0: spisok.append(i)
        i=i-1
    return spisok


def spisok_prostuh(c):
    spisok_prost=[]
    i=c
    while i>0:
        l = prostoe(i)
        l.reverse()
        

        if len(l)==2 and l[0]==1 and l[1]==i : spisok_prost.append(i)
        i=i-1
    return spisok_prost


if regim=="1":
    res = prostoe(x)
    res.reverse()
    k = len(res)
    if k==2 and res[0]==1 and res[1]==x: print(f"Число {x} - простое!")
    if k>2: print(f"Число {x} - не простое!")
    if input("Вывести список всех делителей? Да-1/Нет-любая клавиша:  ")=="1": print(res)
    
if regim !="1":
    z = spisok_prostuh(x)
    print(f"В промежтке целых чисел от 1 до {x} простыми являются следующие числа: \n", z)
