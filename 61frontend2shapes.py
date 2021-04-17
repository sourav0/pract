# from tkinter import *
# win=Tk()
# can=Canvas(win,bg="#7ffc03x")
# # can.create_line(10,200,300,400)
# # can.create_oval(100,150,300,50)
# can.create_polygon(10,20,30,40,50,60)
# can.pack()
# win.mainloop()

# from tkinter import *
# win=Tk()
# can=Canvas(win,height=500,width=500,bg="Red")
# # arc = can.create_arc((5,10,150,200),start = 0,extent = 150, fill= "white")
# l=can.create_line(10,10,200,200,400,10,10,200,width=3,fill="blue")
# # o=can.create_oval(2,2,50,50,fill="blue")
# # s=can.create_rectangle(100,100,200,200,fill="blue")
# # s=can.create_oval(100,100,200,200,fill="blue")
# # a=can.create_arc(100,100,250,200,extent=190,fill="blue")
# #p=can.create_polygon(50,50,0,100,50,150)
# can.pack()
# win.state('zoomed')
# print(dir(Canvas))
# win.mainloop()


# from tkinter import *
# window=Tk()
# canv=Canvas(window,height=800,width=1600,bg="blue")
# l=canv.create_line(50,50,100,100,width=5,fill="red")
# l=canv.create_oval(50,50,100,100)
# canv.pack()
# window.mainloop()

from tkinter import*
c=Tk()

c.geometry("500x500")
form=Canvas(c,width=300,height=300)
name=Label(c,text="Name")
name.place(x=20,y=40)
age=Label(c,text="age")
age.place(x=20,y=70)
gender=Label(c,text="Gender")
gender.place(x=20,y=100)
email=Label(c,text="Email")
email.place(x=20,y=130)

def clear():
    e1.delete(0,END)
    e2.delete(0,END)
    e3.delete(0,END)

def show():
    g=var.get()
    s=e1.get()
    s1=e2.get()
    s2=e3.get()
    course=cvar.get()
    if(g==1):
        gender='Male'
    else:
        gender='Female'
    w='\n'+s+'\t'+s1+'\t'+gender+'\t'+course+'\t'+s2
    f=open(("formdata.txt"),'a')
    f.write(w)
    f.close()
sbmitbtn = Button(c, text = "Submit",command=show,activebackground = "pink", activeforeground = "blue").place(x = 30, y = 230)
reset = Button(c, text = "Reset",activebackground = "pink",command=clear, activeforeground = "blue").place(x = 100, y = 230)
e1=Entry(c)
e1.place(x=70,y=40)
e2=Entry(c)
e2.place(x=70,y=70)
var = IntVar()
r1 = Radiobutton(c, text="Male", variable=var, value=1)
r1.place(x=70,y=100)
r2 = Radiobutton(c, text="Female", variable=var, value=2)
r2.place(x=130,y=100)
e3=Entry(c)
e3.place(x=70,y=130)
cvar = StringVar()
cvar.set("Select course")
option = ("Python", "Javascript", "Perl","Java")
o = OptionMenu(c,cvar, *option)
o.config(font=("times",11),bd=3)
o.place(x=30,y=170,width=190)
c.mainloop()