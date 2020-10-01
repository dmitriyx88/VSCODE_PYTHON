b = input("Введите сторону квадрата в сантиметрах: ")
b= float(b)
import math

def squear(a):
    k = (a*4, a*a, round(a*math.sqrt(2),5))
    return k

r=squear(b)
print("Периметр квадрата = {}; Площадь квадрата = {}; Диагональ квадрата = {}".format(r[0], r[1], r[2]))
