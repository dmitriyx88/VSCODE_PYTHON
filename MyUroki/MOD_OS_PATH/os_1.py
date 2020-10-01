import os
a= os.getcwd()

os.chdir(r"c:\\Windows")
b= os.getcwd()

os.chdir(os.path.dirname(__file__))
c= os.getcwd()

d= c.split(os.path.sep)

e= os.path.join(os.path.dirname(__file__), "fon.jpg")

os.chdir("c:\\")
z= os.listdir()

print(a)
print(b)
print(c)
print(d)
print(os.path.getsize(e))
print(e)
print(z)
