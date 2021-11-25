# for empty list
A = list()
print(A)
print(type(A))

# list patteren Creating
b =[10,20,"jayaram","sandeep","sarojamma",50]
print(b)

#list accessing
print(b[2])
#slicing list
print(b[-2:])

# reassigning list
b[0] = "jayaram is hero"
print(b)

#deleting list
del(b[5])
print(b)

 #operators in list
# adding
c=[10,20]
d=[30,40]
print(c+d)

# *
c=[10,20]
d=[30,40]
print(c*2)

#len()

print(len(b))

# max

print(max(c))

# min

print(min(c))

# sum

print(sum(c+d))

#membership

print(10 in c)
print('jayaram' in b)

for i in b:
    print(i)

# append
A.append(10)

#extended

A.extend([20,30])
print(A)
#remove

A.remove(30)
print(A)

#insert

A.insert(2,30)

print(A)

#reverse

z = A.reverse()

print(z)

#sort
S = A.sort()
print(S)


#count
print(A.count(10))


#index
print(A.index(10))

#list Comprehensions

x = [i+i for i in range(1,20)]
print(x)

X = [i+i for i in b]
print(X)

#removing duplicates

e = [10,20,30,40,30,20,10]
def remove(dup):
    nodup = []
    for element in dup:
        if element not in nodup:
            nodup.append(element)
    return nodup
print(remove(e))

#using set to remove duplicates

li = [1,2,3,1,2,3,5,12,3,5,1,6,6,41,5,3,1,5]
s = set(li)
print(s)
li =list(s)
print(li)

#nested list

dd = [[0,1,2],[3,4,5]]
print(dd[0])
print(dd[0][1])
print(dd[0][2])
print(dd)

ddd= [[[1,0,2,3],[4,5,6,7]],[[1,2,3,4,5],[6,7,8]],[[1,2,3],[3,5,6]]]
print(ddd[0])
print(ddd[0][1])
print(ddd[0][1][1])
print(ddd)


