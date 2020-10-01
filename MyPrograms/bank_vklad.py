money = input("Сумма вклада (грн.):")
period = input("Период вклада (лет):")
percent = input("Ставка % (годовых):")
regim = input("Режим расчета депозита (годовой введите-1 или месячное рефинансирование введите любую клавишу):")

if money.isnumeric(): money= float(money)
else:
     while money.isnumeric()==False:
        money = input("Введите правильную сумму вклада (грн.):")

if period.isnumeric(): period= float(period)
else:
     while period.isnumeric()==False:
        period = input("Введите правильный период вклада (лет):")

if percent.isnumeric(): percent= float(percent)
else:
     while percent.isnumeric()==False:
        percent = input("Введите правильную процентную ставку:")


if regim=="1":
    count=1
    while count<=period:
        money=money+(money/100*percent)
        count=count+1

if regim!="1":
    count=1
    month_perc= percent/12
    while count<=period*12:
        money=money+(money/100*month_perc)
        count=count+1

print(f"По окончанию срока вклада ваш баланс будет соствлять: {round(money,2)} гривен.")