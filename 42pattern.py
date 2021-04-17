# #1st pattern
# # print("Square Pattern")
#
#
# n=int(input("enter no"))
#
# print("patter 1")
# for i in range(n):
#     print("* "*n)
#
# print(" pattern 2 rectangle pattern")
#
# for i in range(n):
#     print("* "*(n+2))
# #
# print("pattern 3")
# print("right angle triangle")
# for i in range(n):
#     print("* "*(i+1))
# #
# #
# print(" pattern 4 revrese right angle triangle")
#
# for i in range(n):
#     print("* "*(n-i))
# #
# print("pattern 5 k shaped pattern")
# for i in range(n):
#     print("* "*(n-i))
# for i in range(n-1):
#     print("* "*(i+2))
# #
# print("pattern no6")
# for i in range(n):
#     print(" "*(n-i-1)+"*"*(i+1))
# #
# #
# # # pattern no 7
# print("pattern no 7")
# for i in range(n):
#     print(" "*(i)+"*"*(n-i))
# #
# # #patter no 8
# print("pattern no 8")
# for i in range(n):
#     print((str(i+1)*(i+1)))
# #
# # #pattern 9
# print("pattern 9")
# for i in range(n):
#     for j in range(i+1):
#         print(j+1,end='')
#     print()
# #
# #
# #pattern10
# print("pattern no 10")
# for i in range(n):
#      print("A "*(i+1))
# #pattern no 11
# print("pattern 11")
# num=1
# for i in range(n):
#     for j in range(0,i+1):
#         print(num,end='')
#         num=num+1
#     print()
#
#
# #pattern no12
# print("pattern no 12")
# num=int(input("enter lst number where to start"))
# for i in range(n):
#     for j in range(i):
#         print(" ",end=' ')
#     for j in range(n-i):
#         print(num,end=' ')
#         num-=1
#     print()
#
# #pattern no13
# print("pattern no13")
# for i in range(n):
#     print((" "*(n-i-1)),end="")
#     for j in range(i+1):
#         print(chr(65+j),end=" ")
#     print()
#
# #pattern no.14
# print("pattern no 14")
# for i in range(n):
#     for j in range(i):
#         print(" ",end="")
#     for j in range(n-i):
#         print(j+1,end="")
#     print()
#
# # pattern no 15
# # for i in range(1,n+1):
# #     for j in range(1,i-1):
# #         print(j,end='')
# #     for j in range(i-1,0,-1):
# #         print(j,end='')
# #     print()
#
# # pattern no 15
# print("pattern no 15")
# for i in range(1,n+1):
#     for j in range(1,i-1):
#         print("*",end='')
#     for j in range(i-1,0,-1):
#         print("*",end='')
#     print()
# # patter no 16
# print("pattern no16")
# for i in range(n):
#     print((" "*(n-i-1)),end="")
#     for j in range(i+1):
#         print(chr(65+j),end=" ")
#     print()
# for i in range(n-1):
#     print((" "*(i+1)),end='')
#     for j in range(n-i-1):
#         print(chr(65+j),end=' ')
#     print()
#
# # pattern no 17
# print("pattern no17")
# print("*" * n, end="\n")
# i = (n // 2) - 1
# j = 2
# while(i!=0):
#     while(j<=(n - 2)):
#         print("*" * i, end="")
#         print(" " * j, end="")
#         print("*" * i, end="\n")
#         i = i - 1
#         j = j + 2
#
# #pattern 18
# print("pattern no 18")
# for i in range(n):
#     print((" "*i)+(chr(90-i)*(n-i)))
#
# #pattern 19
# 10 9 8 7
#   6 5 4
#     3 2
#       1
# n=10
# for i in range(4):
#     for j in range(i):
#         print(" ",end='')
#     for x in range(4-i):
#         print(n,end='')
#         n-=1
#     print()

# diamond pattern
# n=int(input("enmter no"))
# c=1
# for i in range(n):
#     print(' '*(n-i-1),end=' ')
#     for j in range(i+1):
#         print(c,end=' ')
#         c+=1
#     print()
# for i in range(n-1):
#     print(' '*(i+1),end=' ')
#     for j in range(n-1-i):
#         print(c,end=' ')
#         c+=1
#     print()
# for i in range(n-1):
    # print(' '*(i+1)+(str()*(n-i))

# spiral pattern
def pattern(value):
    # Declare a square matrix
    row = 2 * value - 1
    column = 2 * value - 1
    arr = [[0 for i in range(row)]
           for j in range(column)]

    for k in range(value):

        # store the first row
        # from 1st column to
        # last column
        j = k
        while (j < column - k):
            arr[k][j] = str(k+1)
            j += 1

        # store the last column
        # from top to bottom
        i = k + 1
        while (i < row - k):
            arr[i][row - 1 - k] = str(k+1)
            i += 1

        # store the last row
        # from last column
        # to 1st column
        j = column - k - 2
        while j >= k:
            arr[column - k - 1][j] = str(k+1)
            j -= 1

        # store the first column
        # from bottom to top
        i = row - k - 2
        while i > k:
            arr[i][k] = str(k+1)
            i -= 1

    # print the pattern
    for i in range(row):
        for j in range(column):
            print(arr[i][j], end=" ")
        print()


# Driver code
if __name__ == "__main__":
    n = int(input('enter bo'))
    pattern(n)
