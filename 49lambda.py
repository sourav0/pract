x=lambda a,b:a*b
print(x(6,6))

x=lambda a,b,c,d:a+b+c+d
print(x(3,3,8,6))

mylist=[1,2,3,4,5,6,7,8,9]
newlist=list(filter(lambda x:(x%2==0),mylist))
print(newlist)

mylist=[1,2,3,4,5,6,7,8,9]
newlist=list(filter(lambda x:(x%2!=0),mylist))
print(newlist)


mylist=[1,3,6,7]
newlist=list(map(lambda x:(x*2),mylist))
print(newlist)

from functools import reduce
s=reduce(lambda a,b:(a*b),mylist)
print(s)