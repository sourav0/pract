# l=int(input("enter lower limit"))
# u=int(input("enter upper limit"))
# str=[1]
# for n in range(l,u+1):
#     if(n>1):
#         for i in range(2,n):
#             if(n%i==0):
#                 break
#         else:
#             print(n)
#
#
#2nd method
import math
def is_not_prime(n):
    ans = False
    for i in range(2, int(math.sqrt(n)) + 1):
        if n % i == 0:
            ans = True
    return ans
l=int(input("enter lower limit"))
u=int(input("enter upper  limit"))
print("Nonprime numbers ")
for x in filter(is_not_prime, range(l,u+1)):
    print(x)