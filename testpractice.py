#wap to find greatest of 3 no
# x=int(input("enter no"))
# y=int(input("enter no"))
# z=int(input("enter no"))
#
# if x>y:
#     if x>z:
#         print(x,"is greatest no")
#     else:
#         print(z,"is gratest no")
# else:
#     if y>z:
#         print(y,"is greatest no")
#     else:
#         print(z,"is greatest no")

#wap to sum all the numbers in a list

# a=(1,4,6,8)
# from functools import reduce
# x=reduce(lambda b,c:(b+c),a)
# print(x)
# def sum(num):
#     total=0
#     for x in num:
#         total+=x
#     return total
# print(sum(a))

#wap to multiply all numbers in a list
# a=(1,4,6,2)
# def mul(num):
#     total=1
#     for x in num:
#         total=total*x
#     return total
# print(mul(a))

#wap to reverse a string
# a="hello world!"
# def rev(string):
#     b=''
#     index=len(string)
#     while index>0:
#         b+=string[index-1]
#         index=index-1
#     return b
# print(rev(a))

#Write a Python function to calculate the factorial of a number (a non-negative integer).
# The function accepts the number as an argument.
# def factorial(x):
#     if x==0:
#         print("factorial of",x,"is 1")
#     elif x<0:
#         print("please enter valid input")
#     else:
#         i=1
#         f=1
#         while i<=x:
#             f=f*i
#             i=i+1
#         return f
# n=int(input("enter input"))
# print(factorial(n))

# def test_range(a):
#     lower=int(input("enter lower limit of range"))
#     upper=int(input("enter upper limit of range"))
#     if a in range(lower,upper):
#         print("%s is in range "%str(a))
#     else:
#         print("not in range")
# n=int(input("enter no"))
# print(test_range(n))
import pymysql
from tkinter import *

win = Tk()

win.geometry("350x350")
can = Canvas(win, width="300", height="350")
num = Label(win, text="registration form", font="lucida 12 bold")
num.place(x=100, y=2)
num1 = Label(win, text="name", font="lucida 10 bold")
num1.place(x=40, y=30)
num2 = Label(win, text="age", font="lucida 10 bold")
num2.place(x=40, y=70)
num3 = Label(win, text="gender", font="lucida 10 bold")
num3.place(x=40, y=110)
num4 = Label(win, text="course", font="lucida 10 bold")
num4.place(x=40, y=150)
num5 = Button(win, text="c++")
num5.place()

num5 = Label(win, text="contect no", font="lucida 10 bold")
num5.place(x=40, y=200)


def clear():
    d1.delete(0, END)
    d2.delete(0, END)

    d5.delete(0, END)


def show():


# button
num6 = Button(win, text="sign up", command=show, font="lucida 15 bold", bg="blue")
num6.place(x=70, y=250)
# num7=Button(win,text="clear",command=clear,font="lucida 15 bold",bg="red")
# num7.place(x=180,y=250)
var = IntVar()
r1 = Radiobutton(win, text="Male", variable=var, value=1)
r1.place(x=110, y=110)
r2 = Radiobutton(win, text="Female", variable=var, value=2)
r2.place(x=160, y=110)
r3 = Radiobutton(win, text="c++", variable=var, value=3)
r3.place(x=110, y=145)
r4 = Radiobutton(win, text="c", variable=var, value=4)

r4.place(x=170, y=145)
r5 = Radiobutton(win, text="java", variable=var, value=5)
r5.place(x=210, y=145)
r6 = Radiobutton(win, text="python", variable=var, value=6)
r6.place(x=110, y=165)

# entry
d1 = Entry(win)
d1.place(x=120, y=30)
d2 = Entry(win)
d2.place(x=120, y=70)
# d3=Entry(win)
# d3.place(x=120,y=110)
# d4=Entry(win)
# d4.place(x=120,y=150)
d5 = Entry(win)
d5.place(x=120, y=200)
can.pack()
win.mainloop()