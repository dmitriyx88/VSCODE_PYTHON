print("Добро пожаловать в игру Х/О (крестики/нолики)")
print("Указывайте индекс поля для того чтоб совершить ход")
#print("    1|    2|    3")
#print("     |     |     ")
#print("_____|_____|_____")
#print("    4|    5|    6")
#print("     |     |     ")
#print("_____|_____|_____")
#print("    7|    8|    9")
#print("     |     |     ")

x = dict()
for y in range(1,10):
    x[y]=" "

class igra():
    def __init__(self,name):
        self.name= name
    
    def PrintP(self):
        print("    1|    2|    3")
        print(f"  {x[1]}  |  {x[2]}  |  {x[3]}  ")
        print("_____|_____|_____")
        print("    4|    5|    6")
        print(f"  {x[4]}  |  {x[5]}  |  {x[6]}  ")
        print("_____|_____|_____")
        print("    7|    8|    9")
        print(f"  {x[7]}  |  {x[8]}  |  {x[9]}  ")
        return 

    def x_step(self):
        cnt=True
        while cnt==True:
            n = input("Игрок №1, ваш ход. Введите индекс поля для того чтоб поставить -Х:  ")
            if n.isnumeric(): n=int(n)
            else: continue
            if n<10 and x[n]!="X" and x[n]!="O" and n>0:
                x[n]="X"
                cnt=False

    def o_step(self):
        cnt=True
        while cnt==True:
            n = input("Игрок №2, ваш ход. Введите индекс поля для того чтоб поставить -O:  ")
            if n.isnumeric(): n=int(n)
            else: continue
            if n<10 and x[n]!="X" and x[n]!="O" and 0<n<10:
                x[n]="O"
                cnt=False

    def results(self,pl):
        if pl=="X":
            if (x[1]=="X" and x[2]=="X" and x[3]=="X") or (x[4]=="X" and x[5]=="X" and x[6]=="X") or (x[7]=="X" and x[8]=="X" and x[9]=="X") or (x[1]=="X" and x[4]=="X" and x[7]=="X") or (x[2]=="X" and x[5]=="X" and x[8]=="X") or (x[3]=="X" and x[6]=="X" and x[9]=="X") or (x[1]=="X" and x[5]=="X" and x[9]=="X") or (x[3]=="X" and x[5]=="X" and x[7]=="X"):
               print("Игрок №1 выиграл!!!")
               return True
            else: False
        if pl=="O":
            if (x[1]=="O" and x[2]=="O" and x[3]=="O") or (x[4]=="O" and x[5]=="O" and x[6]=="O") or (x[7]=="O" and x[8]=="O" and x[9]=="O") or (x[1]=="O" and x[4]=="O" and x[7]=="O") or (x[2]=="O" and x[5]=="O" and x[8]=="O") or (x[3]=="O" and x[6]=="O" and x[9]=="O") or (x[1]=="O" and x[5]=="O" and x[9]=="O") or (x[3]=="O" and x[5]=="O" and x[7]=="O"):
               print("Игрок №2 выиграл!!!")
               return True
            else: False




p=igra("X/O")
p.PrintP()
while True:
    p.x_step()
    p.PrintP()
    if p.results("X"): break
    p.o_step()
    p.PrintP()
    if p.results("O"): break

input("")
