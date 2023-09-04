#importing the modules 

from tkinter import *
f=s=oper=None


#initializing the functions
def get_digit(d):
    c=rl["text"]
    n=c+str(d)
    rl.config(text=n)

def clear():
    rl.config(text="")

def get_oper(o):
    global f,oper
    f=int(rl["text"])
    oper=o
    rl.config(text="")

def get_res():
    global f,s,oper
    s=int(rl["text"])

    if oper == "+":
        rl.config(text=str(f+s))
    elif oper=="-":
        rl.config(text=str(f-s))
    elif oper=="*":
        rl.config(text=str(f*s))
    else:
        if s==0:
            rl.config(text="Error")
        else:
            rl.config(text=str(round(f/s,2)))

#initializing the task
gui=Tk()

#setting title,size and background color of the window
gui.title("CALCULATOR")
gui.geometry("400x500")
gui.resizable(0,0)
gui.config(bg="azure1")

rl=Label(gui,text="",bg="azure1",fg="black") #164B60 ,#A2FF86
rl.grid(row=0,column=0,columnspan=5,pady=(50,25),sticky="w")
rl.config(font=("Times New Roman",30,"bold"))

b7=Button(gui,text="7",bg="lightblue",fg="black",width=8,height=3,command=lambda:get_digit(7))
b7.grid(row=1,column=0)
b7.config(font=("Times New Roman",15))

b8=Button(gui,text="8",bg="lightblue",fg="black",width=8,height=3,command=lambda:get_digit(8))
b8.grid(row=1,column=1)
b8.config(font=("Times New Roman",15))

b9=Button(gui,text="9",bg="lightblue",fg="black",width=8,height=3,command=lambda:get_digit(9))
b9.grid(row=1,column=2)
b9.config(font=("Times New Roman",15))

b_add=Button(gui,text="+",bg="black",fg="white",width=8,height=3,command=lambda:get_oper("+"))
b_add.grid(row=1,column=3)
b_add.config(font=("Times New Roman",15))

b4=Button(gui,text="4",bg="lightblue",fg="black",width=8,height=3,command=lambda:get_digit(4))
b4.grid(row=2,column=0)
b4.config(font=("Times New Roman",15))

b5=Button(gui,text="5",bg="lightblue",fg="black",width=8,height=3,command=lambda:get_digit(5))
b5.grid(row=2,column=1)
b5.config(font=("Times New Roman",15))

b6=Button(gui,text="6",bg="lightblue",fg="black",width=8,height=3,command=lambda:get_digit(6))
b6.grid(row=2,column=2)
b6.config(font=("Times New Roman",15))

b_sub=Button(gui,text="-",bg="black",fg="white",width=8,height=3,command=lambda:get_oper("-"))
b_sub.grid(row=2,column=3)
b_sub.config(font=("Times New Roman",15))

b1=Button(gui,text="1",bg="lightblue",fg="black",width=8,height=3,command=lambda:get_digit(1))
b1.grid(row=3,column=0)
b1.config(font=("Times New Roman",15))

b2=Button(gui,text="2",bg="lightblue",fg="black",width=8,height=3,command=lambda:get_digit(2))
b2.grid(row=3,column=1)
b2.config(font=("Times New Roman",15))

b3=Button(gui,text="3",bg="lightblue",fg="black",width=8,height=3,command=lambda:get_digit(3))
b3.grid(row=3,column=2)
b3.config(font=("Times New Roman",15))


b_mul=Button(gui,text="*",bg="black",fg="white",width=8,height=3,command=lambda:get_oper("*"))
b_mul.grid(row=3,column=3)
b_mul.config(font=("Times New Roman",15))

b_clear=Button(gui,text="C",bg="black",fg="white",width=8,height=3,command=lambda:clear())
b_clear.grid(row=4,column=0)
b_clear.config(font=("Times New Roman",15))

b0=Button(gui,text="0",bg="lightblue",fg="black",width=8,height=3,command=lambda:get_digit(0))
b0.grid(row=4,column=1)
b0.config(font=("Times New Roman",15))

b_eq=Button(gui,text="=",bg="black",fg="white",width=8,height=3,command=get_res)
b_eq.grid(row=4,column=2)
b_eq.config(font=("Times New Roman",15))

b_div=Button(gui,text="/",bg="black",fg="white",width=8,height=3,command=lambda:get_oper("/"))
b_div.grid(row=4,column=3)
b_div.config(font=("Times New Roman",15))

gui.mainloop()





