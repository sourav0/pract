import re
from tkinter import *
from tkinter import messagebox
def check():
    a=e1.get()
    pattern = '[A-Z]+$'

    # searching pattern
    if re.search(pattern, a):
        messagebox.showinfo("","condition true")
    else:
        messagebox.showinfo("","condition false")
def ch2():
    b = e2.get()
    pattern = '[A-Z]+[a-z]+$'

    # searching pattern
    if re.search(pattern, b):
        messagebox.showinfo("", "condition true")
    else:
        messagebox.showinfo("", "condition false")
def ch3():
    a=e3.get()
    y='[1-9][0-9]{9}'
    if re.compile(a):
        messagebox.showinfo("", "condition true")
    else:
        messagebox.showinfo("", "condition false")
w=Tk()
w.geometry("400x400+0+0")
name=Label(w,text="name").place(x=10,y=10)
e1=Entry(w)
e1.place(x=50,y=10)
name1=Label(w,text="name1").place(x=10,y=40)
e2=Entry(w)
e2.place(x=50,y=40)
Button(w,text='Check',command=check).place(x=200,y=10)
Button(w,text='Check',command=ch2).place(x=200,y=40)
p_no=Label(w,text="Phone no.").place(x=10,y=70)
e3=Entry(w)
e3.place(x=80,y=70)
Button(w,text="check",command=ch3).place(x=250,y=70)
w.mainloop()