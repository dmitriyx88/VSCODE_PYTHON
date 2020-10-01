import turtle
import time
t = turtle.Pen()

def star(size, fil,color):
    if fil:
            t.begin_fill()
    t.color(color)
    for x in range(1,19):
        t.forward(size)
        if x%2==0:
            t.left(175)
        else:
            t.left(225)   
    if fil:
        t.end_fill()

def nuglov(size,fil,color):
    t.color(color)
    if fil:
        t.begin_fill()
    
    for x in range(0,9):
        t.forward(size)
        t.left(45)
    
    if fil:
        t.end_fill()
    
star(100,True,"red")
star(100,False,"blue")
time.sleep(20)
t.reset()
nuglov(100,True,"blue")




time.sleep(5)