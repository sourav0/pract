n=int(input("enter no"))
sum=0
temp=n
while(n):
    i=1
    fact=1
    rem=n%10
    while(i<=rem):
        fact=fact*i
        i=i+1
    sum=sum+fact
    n=n//10
if(sum==temp):
    print("strong no")
else:
    print("not a strong no")