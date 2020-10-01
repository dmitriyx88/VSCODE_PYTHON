import turtle
import time
t = turtle.Pen()

def sq(size,field):
    if field:
        t.begin_fill()
    for x in range(1,5):
        t.forward(size)
        t.left(90)
    if field:
        t.end_fill()
        

#sq(25)
#sq(50)
#sq(75)
#sq(100)
t.color(1,0,0)
sq(125, True)




time.sleep(5)