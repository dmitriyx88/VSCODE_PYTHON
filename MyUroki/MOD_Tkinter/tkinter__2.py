from tkinter import *
import random
import time

root = Tk()

    
def arc1(event, x1, y1):
    for x in range(0, 1):
        cn.move(1, x1 ,y1)
        root.update()
        time.sleep(0.05)
    

cn = Canvas(root, width=500, height=500)
cn.pack()
cn.create_rectangle(10, 10, 30, 30, fill="blue", outline="black")


cn.bind_all('<KeyPress-Right>', lambda event: arc1(event, 5,0))
cn.bind_all('<KeyPress-Left>', lambda event: arc1(event, -5,0))
cn.bind_all('<KeyPress-Down>', lambda event: arc1(event, 0,5))
cn.bind_all('<KeyPress-Up>', lambda event: arc1(event, 0,-5))



root.mainloop()