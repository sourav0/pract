x=input("enter input")
if(x=="A" or x=="E" or x=="I" or x=="O" or x=="U" or x=="a" or x=="e" or x=="i" or x=="o" or x=="u"):
    print("vowel")
elif(ord(x)>=48 and ord(x)<=57):
    print("invalid input")
else:
    print("consonat")