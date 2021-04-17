n=int(input("enter no"))
if(n>1):
    for i in range(2,n):
        if(n%i==0):
            print("not a prime no")
            break
    else:
        print("prime no")
else:
    print("not a prime no")