m = input("Введите интерисующий месяц: ")

def season(month):
    p = month.isnumeric()
    if p: month=float(month)
    if not p: month=0
    if p and month<13:
        if month==1 or month==2 or month==12: r="Зима"
        if month==3 or month==4 or month==5: r="Весна"
        if month==6 or month==7 or month==8: r="Лето"
        if month==9 or month==10 or month==11: r="Осень"
    else: r="Вы ввели не верное значение месяца"
    return r
result= season(m)
print(f"Текущее время года: {result}")