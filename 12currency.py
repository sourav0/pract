a=int(input("enter the amount"))
if(a>=2000):
    print((a//2000),"notes of Rs. 2000")
    a=a%2000
if(a>=500):
    print((a//500),"notes of Rs. 500")
    a=a%500
if(a>=200):
    print((a//200),"notes of Rs.200")
    a=a%200
if(a>=100):
     print((a//100),"notes of Rs.100")
     a=a%100
if(a>=50):
    print((a//50),"notes of Rs.50")
    a=a%50
if(a>=20):
    print((a//20),"notes of Rs.20")
    a=a%20
if(a>=10):
    print((a//10),"notes of Rs.10")
    a=a%10
if(a>=5):
    print((a//5),"notes of Rs.5")
    a=a%5
if(a>=2):
    print((a//2),"notes of Rs.2")
    a=a%2
if(a>=1):
    print((a//1),"notes of Rs.1")