import turtle
import time
t = turtle.Pen()

def star(size, fil,color,vershin):
    if fil:
            t.begin_fill()
    t.color(color)
    for x in range(0,vershin*2):
        t.forward(size)
        if x%2==0:
            t.left(175)
        else:
            t.right(135)   
    if fil:
        t.end_fill()

star(150,True,"red",9)
#star(100,False,"blue",9)
time.sleep(60)