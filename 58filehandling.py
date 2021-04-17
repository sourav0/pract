# a=open("hell","r+")
# str=a.read(5)
# print(str)
# a.close()
#
# a=open("hell","r")
# print(a.read())
# a.close()


# a=open("hell","w")
# a.write("this is write command")
# a.write(" this is write command")
# a.close()

# a=open("hell","w+")
# a.write("dfa ho")
# a.close()

# a=open("hell","a")
# a.write("\n yha se")
# a.close()

# a=open("hell","a+")
# a.write(" nikal")
# a.close()

# import os
# os.rename("hell","hello")

# storing data in a file
# while True:
#     n=open("hell","a+")
#     n.write("\n")
#     a=input("enter name")
#     n.write(a)
#     z=len(a)
#     n.write((9-int(z))*" ")
#     b=input("enter roll number")
#     n.write(b)
#     n.write("    ")
#     c=input("enter class")
#     n.write(c)
#     # n.write("\n")
#     n.close()
#     a=int(input("enter 1 for adding more data"))
#     if(a!=1):
#         break
#     else:
#         print("data updated")

# taking data from five files and storing it in one file
# a=open("f1","r+")
# b=open("f2","r+")
# c=open("f3","r+")
# d=open("f4","r+")
# e=open("f5","r+")
# f=open("f6","a+")
# f.write("\n")
# f.write(a.read())
# f.write("\n")
# f.write(b.read())
# f.write("\n")
# f.write(c.read())
# f.write("\n")
# f.write(d.read())
# f.write("\n")
# f.write(e.read())
# f.write("\n")
# a.close()
# b.close()
# c.close()
# d.close()
# e.close()
# f.close()