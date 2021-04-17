from tkinter import *
wi=Tk()
can=Canvas(wi,bg="red")
# pack
# can.pack()
# can=Canvas(wi,bg="blue")
# can.pack(side="left")
# can=Canvas(wi,bg="blue")
# can.pack(side="bottom")
# grid
# can=Canvas(wi,bg="red")
#
# can.grid(row=0,column=1)
# can=Canvas(wi,bg="red")
# can.grid(row=5,column=5)
# place
can=Canvas(wi,bg="red")
can.place(x=100,y=100)
can=Canvas(wi,bg="blue")
can.place(x=400,y=100)

wi.mainloop()