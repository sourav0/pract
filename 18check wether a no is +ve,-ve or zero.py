a=int(input("enter no."))
if(a==0):
    print(a,"input is zero")
elif(a>0):
    print(a,"is a positive no.")
else:
    print(a,"is a negative no.")
    print("mode value of",a,"is")
    a=-(a)
    print(a)