from tkinter import *
from PIL import ImageTk

def sld(self,fr3):
    self.fr3=fr3
    self.fr3.geometry("1350x750+0+0")
    self.image1=ImageTk.PhotoImage(file="ds1.png\E:\html project\ducat\fashion website\discountlogo")
    self.image2=ImageTk.PhotoImage(file="ds2.png\E:\html project\ducat\fashion website\discountlogo")

    self.lbl1=Label(self.fr3,image=self.image1)
    self.lbl1.place(x=0,y=0)
w=Tk()
w.geometry("500x500+0+0")

# can.pack()
def log():
    fr2.forget()
    fr1.pack()
    bt1.forget()
    bt2.forget()
    b1.pack()
    bt2.pack()
def sig():
    fr1.forget()
    fr2.pack()
    fr3.forget()
    bt2.forget()
    bt1.forget()
    b1.forget()
    bt1.pack()
    b2.pack()

def wel():
    bt1.forget()
    bt2.forget()
    b1.forget()
    b2.forget()
    fr1.forget()
    fr2.forget()
    fr3.pack()
can=Canvas(w,height=600,width=600,bg="yellow")
bt1=Button(w,text="login page",command=log)
bt1.pack()
bt2=Button(w,text="signup page",command=sig)
bt2.pack()
can.pack()
bg = ImageTk.PhotoImage(file = "E:\sarees.png")

fr1=Frame(w,width=300,height=300,bg="red")

b1=Button(w,text="login",command=wel)
b2=Button(w,text="sign in",command=wel)
fr2=Frame(w,width=300,height=300,bg="yellow")
fr3=Frame(w,width=300,height=300,bg="yellow")
lb=Label(fr3,image=bg).pack()
# canvas1 = Canvas(fr3, width=400,height=400)
# canvas1.create_image(150,200,image=bg)
w.mainloop()