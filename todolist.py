#importing the modules
from tkinter import *
from tkinter import messagebox

#defining an empty list
tasklist=[]

#adding task function
def AddTask():
    t=e.get()
    if t!="":
        l.insert(END,t)
        e.delete(0,"end")
    else:
        messagebox.showinfo("ERROR","PLEASE ENTER THE TASK")
    return

#editing the task fumction
def EditTask():
    sel_task=l.curselection()
    if sel_task:
        seltaskindex=sel_task[0]
        edit_task=e.get()
        if edit_task!="":
            l.delete(seltaskindex)
            l.insert(seltaskindex,edit_task)
            e.delete(0,'end')
        else:
            messagebox.showinfo("ERROR","PLEASE ENTER THE TASK")
    else:
        messagebox.showinfo("ERROR","PLEASE ENTER THE TASK")
    return   
#deleting task function
def DelTask():
    l.delete(ANCHOR)
    return

#exit task function
def exit_function():
    gui.destroy()
    return

#initializing the task
gui=Tk()
#setting title,size and background color of the window
gui.title("TO-DO LIST")
gui.geometry("900x750")
gui.config(bg="ghostwhite",pady=50)
gui.resizable(width=False,height=False)

#creating frame widget
f=Frame(gui)
f.pack()

#Label
l1=Label(f,text= "TO-DO LIST",font=("Bookman Old Style",28),pady="18")
l1.pack()

#listbox
l=Listbox(f,width="40",height="11",font=("Bookman Old Style",10),fg="black",bd=2)
l.pack(fill=BOTH)

for t in tasklist:
    l.insert(END,t)

s=Scrollbar(f)
s.pack(side=RIGHT,fill=BOTH)
l.config(yscrollcommand=s.set)
s.config(command=l.yview)

#creating entry box
e=Entry(gui,font=("Bookman Old Style","20"))
e.pack(pady=20)

#creating button
b1=Frame(gui)
b1.pack(pady=20)

l2=Label(gui,text="BY RAMYA GUNDA",font=("Bookman Old Style","11"),fg="black")
l2.pack()

#adding button to the task
addtask=Button(b1, text="ADD TASK",font=("Bookman Old Style","16"),bg="green",padx=20,pady=10,command=AddTask)
addtask.pack(fill=BOTH,expand=True,side=LEFT)

#adding button to edit-task
edittask=Button(b1,text="EDIT TASK",font=("Bookman Old Style","16"),bg="yellow",padx=20,pady=10,command=EditTask)
edittask.pack(fill=BOTH,expand=True,side=LEFT)

#adding button to delete task
deltask=Button(b1,text="DELETE TASK",font=("Bookman Old Style","16"),bg="red",padx=20,pady=10,command=DelTask)
deltask.pack(fill=BOTH,expand=True,side=LEFT)

#dding button to exit task
exit=Button(b1,text="Exit",font=("Bookman Old Style","16"),bg="blue",padx=20,pady=10,command=exit_function)
exit.pack(fill=BOTH,expand=True,side=LEFT)

gui.mainloop()