#digital clock
from tkinter import *
from time import *

def update():
    t=strftime("%H:%M:%S")
    l.config(text=t)
    root.after(1000,update)             # 1000 =1 second

root=Tk()
root.title("DIGITAL CLOCK")
root.geometry("420x150")
root.resizable(False,False)
l=Label(root,
        font=('Arial',68,"bold"),
        bg="black",
        fg="white",
        bd=25)

l.grid(row=0, column=1)
update()
root.mainloop()

