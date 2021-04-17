l=int(input("enter first angle of triangle"))
b=int(input("enter second angle of triangle"))
h=int(input("enter third angle of triangle"))
if((l+b+h)==180):
    print(l,b,h,"are the valid angles of a triangle")
else:
    print(l, b, h, "are not the valid angles of a triangle")