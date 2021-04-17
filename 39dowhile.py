# n=int(input("enter no "))
# i=0
# while True:
#     print(i)
#     i=i+1
#     if(i>n):
#         break

n=input("enter name")
m1=int(input("enter maths marks"))
m2=int(input("enter english marks"))
m3=int(input("enter hindi marks"))
m4=int(input("enter Science marks"))
m5=int(input("enter GK marks"))

x=(m1+m2+m3+m4+m5)/5

# print("total marks",x)


i=0
while True:
    print(n,"your total marks are",x ,"and your grade is")
    if(x<0):
        print("invalid input")
    elif(x > 100):
        print("enter valid input")
    elif (x >= 90 and x <= 100):
        print("A")
    elif (x >= 80 and x < 90):
        print("B")
    elif (x >= 70 and x < 80):
        print("C")
    elif (x >= 60 and x < 70):
        print("D")

    else:
        print("fail")
    a = int(input("please enter '1' to reprint your result else press '0' "))
    i=i+1
    if(a==0):
        print("Thank you!!")
        break
