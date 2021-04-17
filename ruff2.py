# from tkinter import *
# from time import sleep
# pat=Tk()
# #pat.state("zoomed")
# pat.geometry("700x700")
# pat.resizable(0,0)
# pat.configure(bg="#5954e3")
# while True:
#
#  for a in range (2):
#     for b in range(2):
#         can=Canvas(height=350,width=350,bg="#5954e3")
#         x1=10
#         y1=10
#         x2=340
#         y2=340
#         li=[ "yellow","magenta","white", "black", "red", "green", "blue", "cyan", "yellow","magenta"]
#         for i in range (10):
#            x1=x1+15
#            x2=x2-15
#            y1=y1+15
#            y2=y2-15
#            can.create_rectangle(x1,y1,x2,y2,fill=li[i])
#            can.grid(row=a,column=b)
#            pat.update()
#            sleep(0.3)
# pat.mainloop()


import mysql.connector

# Create the connection object
# myconn = mysql.connector.connect(host="localhost", user="root", passwd="1234",database="login")
# printing the connection object
# print(myconn)
# cur=myconn.cursor()
# print(cur)
# cur = myconn.cursor()
# creating table
# cur.execute("CREATE TABLE log (name VARCHAR(255), email VARCHAR(255),password VARCHAR(255))")
# myconn.close()
from tkinter import *

top = Tk()

def ins():
    name=e1.get()
    email=e2.get()
    passwd=e3.get()
    myconn = mysql.connector.connect(host="localhost", user="root", passwd="1234", database="login")
    cur = myconn.cursor()
    sql = "insert into log(name, email, password) values (%s, %s, %s)"

    # The row values are provided in the form of tuple
    val = (name,email,passwd)

    try:
        # inserting the values into the table
        cur.execute(sql, val)

        # commit the transaction
        myconn.commit()
    except:
        myconn.rollback()

    print(cur.rowcount, "record inserted!")
    myconn.close()
top.geometry("400x250")

name = Label(top, text="Name").place(x=30, y=50)

email = Label(top, text="Email").place(x=30, y=90)

password = Label(top, text="Password").place(x=30, y=130)

sbmitbtn = Button(top, text="Submit",command=ins, activebackground="pink", activeforeground="blue").place(x=30, y=170)

e1 = Entry(top)
e1.place(x=80, y=50)

e2 = Entry(top)
e2.place(x=80, y=90)

e3 = Entry(top)
e3.place(x=95, y=130)

top.mainloop()

# from tkinter import *
# from PIL import ImageTk,Image
#
# canvas = Canvas(width = 325, height = 392, bg = 'blue')
#
# image = ImageTk.PhotoImage(Image.open("E:\\sarees.png"))
# canvas.create_image(0, 0, image = image, anchor = NW)
# canvas.pack()
#
# mainloop()
# from tkinter import *
# from PIL import ImageTk as i
# root = Tk()
# root.geometry("400x400")
# bg = i.PhotoImage(file = "E:\sarees.png")
# canvas1 = Canvas(root, width=400,height=400)
# canvas1.create_image(150,200,image=bg)
#
# canvas1.pack(fill="both", expand=True)
# mainloop()