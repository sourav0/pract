def fact(n):
    if(n==0 or n==1):
        return 1
    else:
        return  n*fact(n-1)
n=int(input("enter no"))
res=fact(n)
print(res)

#
# def fib(n):
#     if(n<=1):
#         return n
#     else:
#         return (fib(n-1)+fib(n-2))
# n=int(input("enter no"))
# for i in range(n):
#     print(fib(i))