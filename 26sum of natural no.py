n=int(input("enter no"))
if(n<0):
	print("enter a positive no")
else:
	sum=0
	while(n>0):
		sum+=n
		n-=1
	print(sum)