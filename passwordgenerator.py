from tkinter import *
import random 
import string
c=string.printable

gui=Tk()
gui.title("Password Generator")
gui.geometry("800x700")

def g():
    len=int(e1.get())
    p=""
    for _ in range(len):
        p+=random.choice(c)
    e2.config(state="normal")
    e2.delete(0,END)
    e2.insert(0,p)
    e2.config(state="readonly")

def a():
    t=e2.get()
    if t:
        exit()

def reset():
    e2.config(state="normal")
    e2.delete(0,END)
    e2.config(state="readonly")

c1=Canvas(gui,width=800,height=700,bg="blue")
c1.create_text(400,70,text="PASSWORD GENERATOR",fill="white",font=("Bold",25))
c1.create_rectangle(80,120,700,450,fill="#FFE5AD")

l1=Label(c1,text="Password Length :",font=("Bookman Old Style",13))
l1.place(x=120,y=280)
e1=Entry(c1,font=("Bookman Old Style",14),width=20)
e1.place(x=300,y=280)

l2=Label(c1,text="Generate Password :",font=("Bookman Old Style",13))
l2.place(x=120,y=370)
e2=Entry(c1,font=("Bookman Old Style",14),width=19)
e2.place(x=320,y=370)
e2.config(state="readonly")

b1=Button(c1,text="Generate",width=10,height=2,bg="green",fg="black",font=("Bookman Old Style",14),command=g)
b1.place(x=150,y=500)

b2=Button(c1,text="Accept",height=2,width=10,bg="green",fg="black",font=("Bookman Old Style",14),command=a)
b2.place(x=350,y=510)

b3=Button(c1,text="Reset",width=10,height=2,bg="green",fg="black",font=("Bookman Old Style",14),command=reset)
b3.place(x=500,y=510)
c1.pack()
gui.mainloop()