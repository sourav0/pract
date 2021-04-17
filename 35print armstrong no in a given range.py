l=int(input("enter lower limit"))
u=int(input("enter upper limit"))
for n in range(l,u+1):
    order=len(str(n))
    sum=0
    t=n
    while(t>0):
        d=t%10
        sum+=d**order
        t//=10

    if(n==sum):
        print(n)