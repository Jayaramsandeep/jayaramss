# for empty tuple

a = tuple()

print(type(a))

# creating tuple

b = (10,20,30,"sandeep","jayaram")

print(b)

#Accessing

print(b[4])

#slicing

print(b[:],b[-1:],b[1:])

#reassigning tuple with list

c= list(b)
print(type(c))

c[3] = "jayaram"
c[4] = "sandeep"

b=tuple(c)
print(b)

#deleting

#del(b[0])

print(c)
del(c[0])
print(c)
b=tuple(c)
print(b)

#nested tuple

cc = ((10,20,30),(40,50,60))
print(cc[0])
print(cc[0][1])
ccc = (((1,0,2,3),(4,5,6,7)),((1,2,3,4,5),(6,7,8)),((1,2,3),(3,5,6)))

print(ccc[0])
print(ccc[1][0])
print(ccc[1][0][1])

print(cc)
print(ccc)

#operators in tuple
# adding
c=(10,20)
d=(30,40)
print(c+d)

# *
c=(10,20)
print(c*2)

#len()

print(len(c))

# max

print(max(c))

# min

print(min(c))

# sum

print(sum(c+d))

#membership

print(10 in c)

#count
print(c.count(10))

#index

print(c.index(10))


# tuple Comprehensions

e = (10,20,30,40,50,50)

for i in e:
    print(i)

for i in range(1,10,2):
    print(i)

#using set to remove duplicates
s = set(e)
e= tuple(s)
print(e)

# genarater expressions

x= (i for i in 'abc')
print(x)
