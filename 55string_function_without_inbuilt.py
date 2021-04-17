# swap case in string without using inbulit function
def swap_case(s):
    result = ""
    for letter in s:
        if letter == letter.upper():
            result += letter.lower()
        else:
            result += letter.upper()
    return result
a='Hello World'
print(swap_case(a))
# counting lenght of string
# Function which return length of string
# def findLength(string):
#
# 	# Initialize count to zero
# 	count = 0
#
# # Counting character in a string
# 	for i in string:
# 		count+= 1
# 	# Returning count
# 	return count
#
# # Driver code
# string = "geeksforgeeks"
# print(findLength(string))
#
#
# # 3
# str=input("Enter the String(Lower case):")
# i=0
# ch=''
#
#
# #convert lower to upper case
# while len(str)>i:
#     if str[i]>='a' and str[i]<='z' :
#         ch+=chr(ord(str[i])-32)
#     else:
#         ch += chr(ord(str[i]))
#     i+=1
# print("upper case String is:", ch)
#
#
# # count 4
# string=input("Enter string:")
# count=0
# for i in string:
#       count=count+1
# print("Length of the string is:")
# print(count)