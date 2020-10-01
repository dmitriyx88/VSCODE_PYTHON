from tkinter import *
import random
import time
width_c=800
height_c=600

class Games:
    def __init__(self):
        self.tk=Tk()
        self.tk.title("Приключение Артема!")
        self.tk.resizable(0,0)
        self.tk.wm_attributes("-topmost",1)
        self.cn = Canvas(self.tk, width=width_c, height=height_c)
        self.cn.pack()
        self.tk.update()
        self.cn.bg = PhotoImage(file=r"games/ProGames/fon.gif")
        self.cn.create_image(1,1, image=self.cn.bg, anchor='nw')
        self.sprites=[]
        self.running= True

    def mainloop(self):
        while 1:
            if self.running==True:
                for x in self.sprites:
                    x.move()
                self.tk.update_idletasks()
                self.tk.update()
                time.sleep(0.01)

class Coords:
    def __init__(self, x1=0, y1=0, x2=0, y2=0):
        self.x1=x1
        self.y1=y1
        self.x2=x2
        self.y2=y2



class Artem():
    def __init__(self):
        self.artem_left = [PhotoImage(file=r"games/ProGames/l1.gif"), PhotoImage(file=r"games/ProGames/l2.gif")]
        self.artem_right = [PhotoImage(file=r"games/ProGames/r1.gif"), PhotoImage(file=r"games/ProGames/r2.gif")]
        self.art= self.artem_left[0]
        self.image = g.cn.create_image(50,10, image=self.art, anchor="nw")

    def move_art(self,key):
        if key == "Left":
            g.cn.move(self.image, -3, 0)
            #if self.image.image == self.artem_left[0]:
            #    g.cn.itemconfigure(image=self.artem_left[1])
            #else:
            self.art=self.artem_left[1]
        if key == "Right":
            g.cn.move(self.image, 3, 0)
        if key == "Up":
            g.cn.move(self.image, 0, -3)
        if key == "Down":
            g.cn.move(self.image, 0, 3)






g=Games()

a=Artem()
g.cn.bind_all('<KeyPress-Left>', lambda event: a.move_art("Left"))
g.cn.bind_all('<KeyPress-Right>', lambda event: a.move_art("Right"))
g.cn.bind_all('<KeyPress-Up>', lambda event: a.move_art("Up"))
g.cn.bind_all('<KeyPress-Down>', lambda event: a.move_art("Down"))

g.mainloop()