# x=int(input("enter no. "))
# if(x==1):
#     print("good morning")
# elif(x==2):
#     print("good afternoon")
# elif(x==3):
#     print("good evening")
# elif(x==4):
#     print("good night")
# else:
#     print("invalid input")


#grading system
x=int(input("enter marks"))
if(x>100):
    print("enter valid input")
elif(x>=90 and x<=100):
    print("A")
elif(x>=80 and x<90):
    print("B")
elif(x>=70 and x<80):
    print("C")
elif(x>=60 and x<70):
    print("D")
else:
    print("fail")