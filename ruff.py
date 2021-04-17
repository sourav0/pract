# class emp1:
#     def __init__(self,id):
#         self.id=id
#     def disp(self):
#         print(self.id)
# class emp2(emp1):
#     def __init__(self,dep,id,name):
#         self.name=name
#         # self.id=id
#         self.dep=dep
#         super(emp2, self).__init__(id)
#     def disp(self):
#         print(self.name)
#         print(self.dep)
#
#
# class emp3(emp2):
#     def __init__(self,id,name,age,dep,salary):
#         self.salary=salary
#         self.age=age
#         super().__init__(self,name,dep,id,salary)
#
#
#     def disp(self):
#         # print(self.dep)
#         print(self.salary)
#         # print(self.id)
#         # print(self.name)
#         print(self.age)
#
#         super(emp3, self).disp()
# a=emp3("sour","IOT",23,40000)
# a.disp()
# # ob=emp3()
# # ob1=emp1()
# # ob2=emp2()
# # ob.emp3(1,"sou",98)

# class Plane:
#     def __init__(self):
#         self.wings = 2
#
#         # fly
#         self.drive()
#         self.flaps()
#         self.wheels()
#
#     def drive(self):
#             print('Accelerating')
#
#     def flaps(self):
#             print('Changing flaps')
#
#     def wheels(self):
#             print('Closing wheels')
#
# ba = Plane()
# sorting list
from tkinter import *


def selection():
    selection = "You selected the option " + str(radio.get())
    label.config(text=selection)


top = Tk()
top.geometry("300x150")
radio = IntVar()
lbl = Label(text="Favourite programming language:")
lbl.pack()
R1 = Radiobutton(top, text="C", variable=radio, value=1,
                 command=selection)
R1.pack(anchor=W)

R2 = Radiobutton(top, text="C++", variable=radio, value=2,
                 command=selection)
R2.pack(anchor=W)

R3 = Radiobutton(top, text="Java", variable=radio, value=3,
                 command=selection)
R3.pack(anchor=W)

label = Label(top)
label.pack()
top.mainloop()