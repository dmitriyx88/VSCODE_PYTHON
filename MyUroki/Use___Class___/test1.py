class Amator:
    def __init__(self,name,work,id):
        self.name=name
        self.work=work
        self.id=id
    def __str__(self):
        return "Amator person:"+ self.name + " Work:" + self.work + " id Persons:" + self.id

Persons={}

while True:
    a= input("Name: ")
    b= input(f"Work for {a}: ")
    c= input(f"{a} ID: ")
   
    Persons[a]=Amator(a,b,c)

    ex=input("E to Exit: ")
    if ex=="E": break

print(Persons)

for x in Persons:
    print(Persons[x])

for x in Persons:
    Persons[x].id=str(Persons[x].id)+"99999"

for x in Persons:
    print(Persons[x])