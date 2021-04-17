# def sum():
#     a=int(input("enter no"))
#     b=int(input("enter no"))
#     c=a+b
#     print(c)
#sum()
#
# def mul():
#     a = int(input("enter no"))
#     b = int(input("enter no"))
#     c = a * b
#     print(c)
#
#
# def sub():
#     a = int(input("enter no"))
#     b = int(input("enter no"))
#     c = a - b
#     print(c)
#
#
# def div():
#     a = int(input("enter no"))
#     b = int(input("enter no"))
#     c = a / b
#     print(c)
# method 2
# a=input
# b=input
# def sum(a,b):
#     c=a+b
#     print(c)
#sum()
# def mul(a,b):
#     c=a*b
#     print(c)
# def sub(a,b):
#     c=a-b
#     print(c)
# def div(a,b):
#     c=a/b
#     print(c)
# method3
# def sum(a,b):
#     c=a+b
#     return c
# def mul(a,b):
#     c=a*b
#     return c
# def sub(a,b):
#     c=a-b
#     return c
# def div(a,b):
#     c=a/b
#     return c
# x=int(input("enter no"))
# y=int(input("enter no"))
# n=int(input("enter 1 for add ,2 for multiply, 3 for sub ,4 for div"))
#
# if(n==1):
#     print(sum(x,y))
# elif(n==2):
#     print(mul(x,y))
# elif(n==3):
#     print(sub(x,y))
# elif(n==4):
#     print(div(x,y))
# else:
#     print("invalid input")




a=int(input("enter no"))
b=int(input("enter no"))
def sum(x,y):
    z=x+y
    return z
c=sum(a,b)
print("sum",c)
def sqr(m):
    m=m**2
    return m
g=sqr(c)
print("square value",g)
def fact(n):
    i = 1
    f = 1
    while (i <= n):
        f = f * i
        i = i + 1
    return f

k=fact(g)
print("factorial value",k)

def oddeven(l):
    if (l % 2 == 0):
        print("even no")
        # sum = 0
        # while (l > 0):
        #     sum += l
        #     l -= 2
        # print(sum)
    else:
        print("odd no")
        # sum = 0
        # while (l > 0):
        #     sum += l
        #     l -= 2
        # print(sum)
    return
oddeven(k)

  

