# Question 1: Given a Python list you should be able to display Python list in the following order
# a=[1,2,3,4,5,]
# a=a[::-1]
# print(a)

# Question 2: Concatenate two lists index-wise

# a=['m','se']
# b=['y','lf']
# c=[i+j for i,j in zip(a,b)]
# print(c)

# Question 3: Given a Python list. Turn every item of a list into its square
# a=[1,2,3,4]
# a=[x*x for x in a]
# print(a)

# Question 4: Concatenate two lists in the following order
# a=['m','se']
# b=['y','lf']
# c=[i+j for i in a for j in b]
# print(c)


# Question 5: Given a two Python list. Iterate both lists simultaneously
# such that list1 should display item in original order and list2 in reverse order
# list1 = [10, 20, 30, 40]
# list2 = [100, 200, 300, 400]
#
# for x, y in zip(list1, list2[::-1]):
#     print(x, y)

# Question 6: Remove empty strings from the list of strings
# a=['cdc','sssssd','','sd','']
# b=list(filter(None,a))
# print(b)


# Question 7: Add item 7000 after 6000 in the following Python List
# list1 = [10, 20, [300, 400, [5000, 6000], 500], 30, 40]
# list1[2][2].append(7000)
# print(list1)