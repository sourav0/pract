#quesstion1
#  Given a string of odd length greater 7, return a string made of the middle three chars of a given String
# def middle_string(s):
#     a=int(len(s)/2)
#     mds=s[a-1:a+2]
#     print(mds)
# z=input("enter string")
# middle_string(z)


# question2
# Given 2 strings, s1 and s2, create a new string by appending s2 in the middle of s1
# s1='hello'
# s2='world'
# def ape(s1,s2):
#     mi=int(len(s1)/2)
#     mit=s1[:mi]+s2+s1[mi:]
#     print(mit)
# ape(s1,s2)
# Question 3: Given 2 strings, s1, and s2 return a new string made of
# the first, middle and last char each input string
# s1='hello'
# s2='world'
# def fml(s1,s2):
#     mi1=int(len(s1)/2)
#     mi2=int(len(s2)/2)
#     new=s1[:1]+s2[:1]+s1[mi1]+s2[mi2]+s1[-1]+s2[-1]
#     print(new)
# fml(s1,s2)

# s=["hello","world"]
# for i in s:
#     for j in i:
#         print(j)3

# Question 4: Arrange string characters such that lowercase letters should come first
# s="Hello_World"
# low=[]
# up=[]
# for i in s:
#     if i.islower():
#         low.append(i)
#     else:
#         up.append(i)
# ns=''.join(low+up)
# print(ns)


# Question 5: Count all lower case, upper case, digits, and special symbols from a given string
# a='sd@3'
# def ans(a):
#     m=0
#     n=0
#     o=0
#     for i in a:
#         if i.islower() or i.isupper():
#             m+=1
#         elif i.isnumeric():
#             n+=1
#         else:
#             o+=1
#     print("chars =",m,"numbers =",n,"symbols =",o)
# ans(a)

# Question 6: Given two strings, s1 and s2, create a mixed String
# def mixString(s1, s2):
#     s2 = s2[::-1]
#     lengthS1 = len(s1)
#     lengthS2 = len(s2)
#     length = lengthS1 if lengthS1 > lengthS2 else lengthS2
#     resultString = ""
#     for i in range(length):
#         if (i < lengthS1):
#             resultString = resultString + s1[i]
#         if (i < lengthS2):
#             resultString = resultString + s2[i]
#
#     print(resultString)
#
#
# s1 = "Abc"
# s2 = "Xyz"
# mixString(s1, s2)




# Question 7: String characters balance Test
# def bal(s1,s2):
# print(bal(s1,s2))

#     flag=True
#     for i in s1:
#         if i in s2:
#             continue
#         else:
#             flag=False
#     return flag
# s1=input("enter first string")
# s2=input("enter 2nd string")


# Question 8: Find all occurrences of “USA” in given string ignoring the case
# a=input("enter your main string")
# b=input("enter sub string")
# temp=a.lower()
# count=temp.count(b.lower())
# print(count)

# Question 9: Given a string, return the sum and average
# of the digits that appear in the string, ignoring all other characters
# import re
#
# inputStr = "English = 78 Science = 83 Math = 68 History = 65"
# markList = [int(num) for num in re.findall(r'\b\d+\b', inputStr)]
# totalMarks = 0
# for mark in markList:
#   totalMarks+=mark
#
# percentage = totalMarks/len(markList)
# print("Total Marks is:", totalMarks, "Percentage is ", percentage)


# Question 10: Given an input string, count occurrences of all characters within a string
# str1 = "hello"
# countDict = dict()
# for char in str1:
#   count = str1.count(char)
#   countDict[char]=count
# print(countDict)

# Question 11: Reverse a given string
# a=input("enter string")
# print("Original String",a)
# a=a[::-1]
# print("reversed string",a)

# Question 12: Find the last position of a substring “Emma” in a given string
# str1 = "Emma is a data scientist who knows Python. Emma works at google."
# print("Original String is:", str1)
#
# index = str1.rfind("Emma")
# print("Last occurrence of Emma starts at", index)


# Question 13: Split a given string on hyphens into several substrings and display each substring
# a=input("enter string")
# print("original string",a)
# substring=a.split(" ")
# print("divide string")
# for i in substring:
#     print(i)

# Question 14: Remove empty strings from a list of strings
# str_list = ["Emma", "Jon", "", "Kelly", None, "Eric", ""]
# print("Original list of sting")
# print(str_list)
#
# # use built-in function filter to filter empty value
# new_str_list = list(filter(None, str_list))
#
# print("After removing empty strings")
# print(new_str_list)

# Question 15: Remove special symbols/Punctuation from a given string
# import string
#
# str1 = "/*Jon is @developer & musician"
# print("Original string is ", str1)
# # use translate function of a string
# # and maketrans function of str class
# new_str = str1.translate(str.maketrans('', '', string.punctuation))
# print("New string is ", new_str)

# Question 16: Removal all the characters other than integers from string
# str1 = 'I am 25 years and 10 months old'
# print("Original string is", str1)
#
# # Retain Numbers in String
# # Using list comprehension + join() + isdigit()
# res = "".join([item for item in str1 if item.isdigit()])
#
# print(res)


# Question 17: Find words with both alphabets and numbers
# str1 = "Emma25 is Data scientist50 and AI Expert"
# print("The original string is : " + str1)
#
# # Words with both alphabets and numbers
# # isdigit() for numbers + isalpha() for alphabets
# # use any() to check each character
#
# res = []
# temp = str1.split()
# for item in temp:
#     if any(char.isalpha() for char in item) and any(char.isdigit() for char in item):
#         res.append(item)
#
# print("Displaying words with alphabets and numbers")
# for i in res:
#     print(i)



# Question 18: From given string replace each punctuation with #
from string import punctuation

# str1 = '/*Jon is @developer & musician!!'
# print("The original string is : ", str1)

# Replace punctuations with #
# replace_char = '#'

# Using string.punctuation to get the list of all punctuations
# use string function replace() to replace each punctuation with #

# for char in punctuation:
#     str1 = str1.replace(char, replace_char)
#
# print("The strings after replacement : ", str1)