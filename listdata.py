# # 1. iterate over 2+ lists at the same time
# #--------------------------------------------
#
# name = ['sandeep','bharath','srikanth','sai']
# pets = ['dog','cat','honeybee','fox']
# age = [25,24,24,24]
#
# # we can use the zip function to iterate
# #----------------------------------------
#
# z = zip(name,pets,age)
# print(z)
#
# for i in z:
#     print("name is %s and pets is %s and age is %s "%i)
#
#
# # shallow copy
# #-----------
#
# name = ['sandeep','bharath','srikanth','sai']
# name2 = name.copy()
# name2[0] = 'sun'
# name[0] = 'jayaram'
# print(name)
# print(name2)
#
# # deep copy
# #----------
#
# name = ['sandeep','bharath','srikanth','sai']
# import copy
# name2 = copy.deepcopy(name)
# name2[0] = 'jayaram'
# print(name)
# print(name2)
#
# # converting list to dictionary
# #------------------------
# li = ['sandeep','bharath','srikanth','sai']
# val = [25,24,24,24]
# d = {k:1 for k in li}
# print(d)
#
#
# # existing list with a lambda function
# #-----------------------------
#
# a = [10,30,20,50,60]
#
# b = list(map(lambda val:val*5,a))
# print(b)
#
# # even numbers remove
# #-------------
#
# li  = [1,2,3,4,5,6,7,8,9,10]
# a = [i for i in li if i %2 !=0]
# print(a)
#
# # odd numbers remove
# #-------------
#
# li  = [1,2,3,4,5,6,7,8,9,10]
# a = [i for i in li if i %2 ==0]
# print(a)
#
# # occurence
# # method 1
# #---------------
#
# list = ['s','a','n','d','e','e','p']
# out = {x: list.count(x) for x in set(list)}
# print(str(out))
# #output
# #                {'n': 1, 's': 1, 'd': 1, 'p': 1, 'a': 1, 'e': 2}
#
# #method 2
# #-------------
#
# list = ['s','a','n','d','e','e','p']
#
# dum= { }
# for ele in list:
#     if ele in dum:
#         dum[ele] += 1
#     else:
#         dum[ele] = 1
# print(str(dum))
# #output
# #                     {'s': 1, 'a': 1, 'n': 1, 'd': 1, 'e': 2, 'p': 1}
#
# from collections import Counter
# list = ['s','a','n','d','e','e','p']
# print(Counter(list))
#
# # combine list into string
# #---------------------------
#
# li = ['sandeep','is','fighter','bharath','is','fight','srikanth','is','fightr','sai','is','fighr']
# print(' '.join(li))
#
#
# z = input('enter the number or int :')
# f = input('enter name:')
# w= z+f
# print(w,''.join(f))
# print(z.join(f))
#
# #remove duplicates
#
# #method 1
# #--------------
#
# list = ['s','a','n','d','e','e','p']
# li = set(list)
# print(li)
#
# #output
# #             {'a', 'e', 's', 'd', 'p', 'n'}
#
# #method 2
# #------------
# list = ['s','a','n','d','e','e','p']
# li = [ ]
# for i in list:
#     if i not in li:
#         li.append(i)
# print(li)
#
# #output
# #                 ['s', 'a', 'n', 'd', 'e', 'p']
#
# #
# we can create empty list object as follows:
#-----------------------------------------

# list = []
# print(list)
# print(type(list))

# []
# <class 'list'>

#if we know elements already then we can create list as follows........
#----------------------------------

#list = [10,20,30,40]

#with dynamic input:

# list =eval(input("Enter list :"))
# print(list)
# print(type(list))


