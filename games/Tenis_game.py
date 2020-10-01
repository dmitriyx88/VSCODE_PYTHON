from tkinter import *
import time
import random
wth_win=500
hght_win=400
rocket_id=0

class Ball:
    def __init__(self, canvas, color):
        self.canvas= canvas
        self.id = canvas.create_oval(10,10,25,25, fill=color)
        self.canvas.move(self.id, 245, 100)
        speed=[-3,-2,-1,1,2,3]
        random.shuffle(speed)
        self.x=speed[0]
        self.y=-3
        self.canvas_height=self.canvas.winfo_height()
        self.canvas_width=self.canvas.winfo_width()
    
    def draw(self):
        self.canvas.move(self.id, self.x,self.y)
        pos=self.canvas.coords(self.id)
        #print(pos)
        if pos[1]<=0:
            self.y=abs(self.y)
        if pos[3]>=hght_win:
            self.y=abs(self.y)*(-1)
        if pos[0]<=0:
            self.x=abs(self.x)
        if pos[2]>=wth_win:
            self.x=abs(self.x)*(-1)
    
    def otskok(self):
        pos=self.canvas.coords(self.id)
        pos_rk=self.canvas.coords(rocket_id)
        #print(pos,pos_rk)
        if pos[3]>=pos_rk[1] and pos[0]>=pos_rk[0] and pos[2]<=pos_rk[2]:
            self.y=abs(self.y)*(-1)
    
    def goal(self):
        pos=self.canvas.coords(self.id)
        if pos[3]>=hght_win:
            schet.faul()

class Rocket:
    def __init__(self,canvas, color):
        self.canvas=canvas
        self.id=self.canvas.create_rectangle(10,hght_win-20,110,hght_win-15,fill=color)
        global rocket_id 
        rocket_id=self.id
    
    def draw_rk(self,key):
        if key =="Left":
            self.canvas.move(self.id,-15,0)
        if key == "Right":
            self.canvas.move(self.id,15,0)

class Schet:
    def __init__(self,canvas,color):
        self.canvas=canvas
        self.cnt=0
        self.color=color
        self.id= self.canvas.create_text(wth_win/2,10, text=f"Вы пропустили мячей: {self.cnt}", fill=color, justify=LEFT)
        
    def faul(self):
        self.cnt=self.cnt+1
        self.canvas.itemconfigure(self.id, text=f"Вы пропустили мячей: {self.cnt}")
        
        print(self.cnt)
        
        

tk=Tk()
tk.title("Большой тенис")
tk.resizable(0,0)
tk.wm_attributes("-topmost",1)

cn = Canvas(tk, width=wth_win, height=hght_win)
cn.pack()
tk.update()


ball= Ball(cn, "red")
rocket =Rocket(cn,"blue")
schet= Schet(cn,"green")

while 1:
    ball.draw()
    ball.otskok()
    ball.goal()
    if schet.cnt >9:
        print("Вы проиграли!")
        break
    cn.bind_all('<KeyPress-Left>', lambda event: rocket.draw_rk("Left"))
    cn.bind_all('<KeyPress-Right>', lambda event: rocket.draw_rk("Right"))
    cn.bind_all('<ButtonPress-1>', lambda event: rocket.draw_rk("Left"))
    cn.bind_all('<ButtonPress-3>', lambda event: rocket.draw_rk("Right"))
    tk.update_idletasks()
    tk.update()
    time.sleep(0.01)


tk.mainloop()