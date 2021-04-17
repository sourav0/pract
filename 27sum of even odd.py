n=int(input("enter no."))
if(n%2==0):
	print("even no")
	sum=0
	while(n>0):
		sum+=n
		n-=2
	print(sum)
else:
	print("odd no")
	sum=0
	while(n>0):
		sum+=n
		n-=2
	print(sum)
