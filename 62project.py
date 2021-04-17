# from tkinter import *
# w=Tk()
# w.geometry("500x500")
# canvas=Canvas(w,width="300",height="500",bg="white")
# canvas.pack()
# # canvas.create_line("x1,y1,x2,y2, fill="color")
# # canvas.create_line(10,200,300,200, fill="red")
# # canvas.create_line(150,20,150,400, fill="red")
# # face
# canvas.create_oval(100,10,200,150,fill="yellow")
# # eyes
# canvas.create_oval(120,50,140,70,fill="blue")
# canvas.create_oval(160,50,180,70,fill="blue")
# # nose
# canvas.create_rectangle(145,70,155,100,fill="blue")
# # mouth
# canvas.create_oval(130,110,170,130,fill="blue")
# # body
# # canvas.create_line(150,150,270,400,fill="red")
# # canvas.create_line(150,150,30,400,fill="red")
# # canvas.create_line(30,400,270,400,fill="red")
#
# # hands
# canvas.create_line(125,170,10,210,fill="red",width=5)
# canvas.create_line(170,170,290,210,fill="red",width=5)
# canvas.create_polygon(150,65,30,400,270,400,fill="red",smooth=1)
# # feet
# canvas.create_line(90,350,90,480,fill="red",width=5)
# canvas.create_line(210,350,210,480,fill="red",width=5)
# w.mainloop()
from tkinter import *

top = Tk()

top.geometry("400x250")
name = Label(top, text="Name").place(x=30, y=50)

email = Label(top, text="Email").place(x=30, y=90)

password = Label(top, text="Password").place(x=30, y=130)

sbmitbtn = Button(top, text="Submit", activebackground="pink", activeforeground="blue").place(x=30, y=170)
resetbtn = Button(top, text="Reset", activebackground="pink", activeforeground="blue").place(x=150, y=170)

e1 = Entry(top).place(x=80, y=50)

e2 = Entry(top).place(x=80, y=90)

e3 = Entry(top).place(x=95, y=130)

top.mainloop()