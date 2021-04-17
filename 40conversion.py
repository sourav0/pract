# def convert(fromnum,frombase,tobase):
#     tonum=0
#     power=0
#     while(fromnum>0):
#         tonum += frombase**power*(fromnum%tobase)
#         fromnum//=tobase
#         power+=1
#     return tonum
#
# n=int(input("enter number u wana convert"))
# b=int(input("enter current base of no 'either 2 or 10'"))
# d=int(input("enter base in which u wana convert 'either 2 or 10'"))
#
# print(convert(n,b,d))

#decimal to octal
dec=int(input("enter number"))
octal=0
ctr=0
temp=dec

while(temp>0):
    octal+=((temp%8)*(10**ctr))
    temp=int(temp/8)
    ctr+=1
print(octal)