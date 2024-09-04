# n = int(input("enter the number"))
# count = 0
# for i in range(1, n):
#     if n % i == 0:
#         count = count+1
# if count == 1:
#     print("prime")
# else:
#     print("composite")


# num = int(input("enter a number : "))
# n = num
# l = len(str(num))
# sum = 0
# while num != 0:
#     rem = num % 10
#     sum = sum+(rem**int(l))
#     num = num//10
# if n == sum:
#     print("armstrong")
# else:
#     print("not armstrong")


# str = input("enter a string : ")
# if str == str[::-1]:  # to reverse a string
#     print("palindrome")
# else:
#     print("not palindrome")


# size = int(input("Enter size : "))
# list = []
# for i in range(0, size):
#     ele = int(input())
#     list.append(ele)
# sum = 0
# for i in range(0, size):
#     sum = sum+list[i]
# print(sum)


# punctuations = "~!@#$%^&*()_+-=[]{}|\;:',./?"
# mystr = input("Enter a String : ")
# ans = ""
# for c in mystr:
#     if c not in punctuations:
#         ans = ans+c
# print(ans)


# num = int(input("Enter a number : "))
# n = str(num)
# ans = n[::-1]
# print(ans)


# for i in range(5):
#     for j in range(i+1):
#         print("*", end=" ")
#     print("")


# import numpy as np
# x = np.random.randint(low=1, high=300, size=10)
# print(x)


# import numpy as np
# X = [[1, 1], [1, 1]]
# trans = np.transpose(X)
# ans = np.ans(X, trans)
# print(ans)


# X = [[1, 2], [3, 4]]
# result = [[0, 0], [0, 0]]
# for i in range(len(X)):
#     for j in range(len(X[0])):
#         result[j][i] = X[i][j]
# for r in result:
#     print(r)

# items = input("Enter a string : ")
# items.split("-")
# items.sort()
# print("-".join(items))


# import re
# text = "  sai  abhi  ram  "
# print(re.sub(" ", "", text))

n=5
for i in range(n):
    for j in range(i+1):
        print("*",end=" ")
    for j in range(i,n):
        print(" ",end=" ")
    for j in range(i,n-1):
        print(" ",end=" ")
    for j in range(i+1):
        print("*",end=" ")
    print()
for i in range(n*2+1):
    print("*",end=" ")
print()
for i in range(n):
    for j in range(i,n):
        print("*",end=" ")
    for j in range(i+1):
        print(" ",end=" ")
    for j in range(i):
        print(" ",end=" ")
    for j in range(i,n):
        print("*",end=" ")
    print()