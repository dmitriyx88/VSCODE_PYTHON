import random

slowar = []
with open(r"Igra_Wisilica\slowar.txt", mode="r", encoding="Utf-8") as opSlowar:
    slowar = opSlowar.read()
    opSlowar.close
    slowar = slowar.split("\n")
    slowo = slowar[random.randint(0, len(slowar))]


class igra:
    def __init__(self, name, slowo):
        self.name=name 
        self.slowo =list(slowo)
        self.max_error: int = 0
        self.slowoX: list =[]

    def createList(self):
        if len(self.slowoX) == 0:
            for _ in range(0, len(slowo)):
                self.slowoX.append(" _ ")
        print(self.slowoX)

    def inpMaxError(self):
        print(f"В слове {len(self.slowo)} букв. ")
        while True:
            e = input("Введите максималное количество ошибочных попыток отгодать букву в слове: ")
            if e.isnumeric():
                e = int(e)
                self.max_error = e
                break
    
    def inp_bukv(self):
        while True:
            b = input("Введите предпологаемую букву: ")
            b.lower()
            if b.isalpha() and len(b)==1:
                break
        if self.slowo.count(b)>0:
            for x, y in enumerate(self.slowo):
                if y==b:
                    self.slowoX[x]=y.upper()
                    print(f"Да, вы угадали! Буква \"{b}\" в этом слове присудствует.")
                    print(self.slowoX, "\n \n \n \n")
        else: 
            print(f"К сожалению вы не угадали. Буква \"{b}\" в слове отсуцтвует.")
            self.max_error = self.max_error-1
    
    def MaxError(self):
        if self.max_error<1:
            print(f"Упс... {i.name}, у вас закончились попытки отгадать слово. \nК сожалению вы проиграли. \nпопробуйте в следующий раз.")
            return False
        else:
            print(f"{i.name} у вас осталось {self.max_error} попыток.\n \n \n \n")
        return True
                



i = igra(input("Введите ваше имя: "), slowo)
#print(i.slowo)
i.createList()
i.inpMaxError()
while True:
    i.inp_bukv()
    if i.MaxError() is not True:
        break
    
    if i.slowoX.count(" _ ")<1:
        print("Победа!!! Вы верно отгадали слово:", i.slowoX)
        break



