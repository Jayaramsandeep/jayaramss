# #Remove Duplicates of an Array.
#
# # s ={1,7,2,3,0,8,1,8,6,7,4,9,2,0,1,6,5}
# # dup = set()
# # uni_items =[]
# # for i in s:
# #     if i not in dup:
# #         uni_items.append(i)
# #         dup.add(i)
# # print(dup)
# #Array: {3,2,6,1,8,4,5}
#
#
#
# #Take 3 Number out of the Array and the
# #Target Sum: 7
#
#
# # def sum(a,b,c):
# #     for i in range(0,b-2):
# #         for j in range(i+1,b-1):
# #             for k in range(j+1,b):
# #                 if a[i] + a[j]  + a[j] == c:
# #                     print("sum = 7 ")
# #                     return True
# #         return False
a = [3,2,6,1,8,4,5]
count=0
b=0
while b<=3:
    for i in a:
        i+=i
        b+=1

#                     count=count+i
#
print("sum = ", i)
#
# # a = [3,2,6,1,8,4,5]
# # for i in a:
# #     print(i)
#     sum=sum+i
lis  = [100,20,10 ,-20,-20,5]
#ou = [-20,-20,10,20,-5]
# l=[1,1,1,0,1,0,1,0,0,1,1,0,1,0,1,0,1]
# o=[0,0,0,0,0,0,0,0,0,1,1,1,1,1,1]
# for i in range(lis):
#     for j in range(0,i):
        
em= [ ]
for i in lis:
    if i in em:


