#1st
# n=568910
# for i in str(n):
#     print(i)
# 2nd question
# n=int(input("enter no"))
# for i in range(0,n):
#     if(i%3==0 and i%5==0):
#         print("excellence technology")
#     elif (i % 3 == 0):
#         print("excellence")
#     elif(i%5==0):
#         print("technology")
#     else:
#         print(i)
#     i+=1
#
# prime factor
# n=int(input("enter number"))
# i=1
# while(i<=n):
#     j=0
#     if(n%i==0):
#         k=1
#         while(k<=i):
#             if(i%k==0):
#                 j=j+1
#             k=k+1
#         if(j==2):
#             print(i)
#     i+=1

# 4
# n=568910
# while(n>0):
#     print(n//10)
#     n-=1
# 5
# n=int(input("enter number"))
# a=3
# b=5
# i=1
# while(i<=n):
#     if(i==a and i==b):
#         print("excellence technology")
#         a+=3
#         b+=5
#     elif(i==a):
#         print("excellence")
#         a+=3
#     elif(i==b):
#         print("technology")
#         b+=5
#     else:
#         print(i)
#     i+=1

import tkinter
from tkinter import *

root = Tk()

root.maxsize(320,240)       # Sets max size of window
root.minsize(320,240)

canvas_height = 23
canvas_width = 315

w = Canvas(root, width=canvas_width, height=canvas_height)
w.pack()
w.create_rectangle(5, canvas_height, canvas_width, 2, fill="yellow")
w.create_rectangle(5, canvas_height, canvas_width, 2, fill="blue")

a = 1.0 # More complicated code creates this float between 0.00 and 1.00. It is a percentage of the desired 'blue rectangle' width
b = int(a * canvas_width)

root.mainloop()