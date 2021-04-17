n=int(input("enter number"))
s=0
t=n
while(t>0):
    d=t%10
    s=s+d**3
    t=t//10
if(s==n):
    print("Armstrong number.")
else:
    print("not a Armstrong number.")