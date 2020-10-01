from tkinter import *
root = Tk()
 
def font1(event):
    l['font'] = "Verdana"
def font2(event):
    l['font'] = "Times"
 
l = Label(text="Hello World")
 
l.bind('<Button-1>', font1) # ЛКМ
l.bind('<Button-3>', font2) # ПКМ
l.pack()
 
root.mainloop()