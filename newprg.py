# def fibonacci(n):
#     if n == 0:
#         return 0
#     elif n == 1:
#         return 1
#     else:
#         a, b = 0, 1
#         for i in range(2, n + 1):
#             a, b = b, a + b
#         return b

# n = int(input("Enter the position in Fibonacci sequence: "))
# print(fibonacci(n))

# list
# my_list = [1, 2, 3, 4, 5]
# print(my_list[4]) 
# # start index is inclusive and end index is exclusive
# print(my_list[1:4])

# #list operations
# #concatenation 
# a = [1,2,3,4]
# b = [5,6,7,8,9]
# print(a+b)

# #repitation usage
# print(a*2)

# #membership
# fruits=["apple","banana","citrus","grape"]
# print("apple" in fruits)
# print("grape" not in fruits)

# #comparision
# list1 = [1,2,3]
# list2 = [1,2,4]
# print(list1 == list2)
# print(list1 < list2)

# #list methods
# # append
# list1.append(4)
# print(list1)

# # insert
# list1.insert(3,5)
# print(list1)

# # extend
# b = [111,2222,333]
# list1.extend(b)
# print(list1)

# # remove
# list1.remove(5)
# print(list1)

# # pop(index)
# list1.pop()
# print(list1)

# # # clear
# # list1.clear()
# # print(list1)

# # index
# print(list1.index(1))

# # count
# print(list1.count(111))

# # sort
# list1.sort(reverse=True)
# print(list1)

# # copy
# x = list1.copy()
# print(x)

# a = 'rvs cet'
# upper = lambda x: x.upper()  
# print(upper(a))

# only one expression at a time
# Implicit return of that expression

# map function
num =[1,2,3,4]
result = list(map(lambda x: x*2, num))
print(result)

# def func(x):
#     return x*2
# result = list(map(func, num))
# print(result)
# numone = [1,2,3,4,5,6,7,8,9,10]
# check = lambda z: "Even" if z % 2 == 0 else "Odd"
# print(list(map(check, numone)))

# reduce (fun,iterate)
# from functools import reduce
# numtwo = [1,2,3,4,5]    
# reduce(func, iterable[, initializer])
# result = reduce(lambda x,y: x+y, numtwo)
# print(result)

# odd numbers 
# filter (fun, iterate)
# num = [1,2,3,4,5,6,7,8,9,10]
# odd = list(filter(lambda x: x % 2 != 0, num))
# print(odd)

# palindrome

# word = input("Enter a word: ")
# if word == word[::-1]:
#     print(word, "is a palindrome.")
# else:
#     print(word, "is not a palindrome.")

# without slicing
# word = input("Enter a word: ")
# reversed_word = ""
# for char in word:
#     reversed_word = char + reversed_word
# if word == reversed_word:
#     print(word, "is a palindrome.")
# else:
#     print(word, "is not a palindrome.")

num = int(input("Enter a number: "))
def palindrome(num):
    temp = num
    rev =0 
    while temp > 0:
        rem = temp % 10
        rev = rev * 10 + rem
        temp = temp // 10
    if num == rev:  
        print(num, "is a palindrome.")
    else:
        print(num, "is not a palindrome.")
palindrome(num)
# 121