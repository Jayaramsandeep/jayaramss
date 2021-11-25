# creating empty set

a = set()
print(type(a))

a.add(10)

a.add(20)
print(a)
a.add(30)
a.add(40)
a.add(50)
print(a)

for i in a:
    print(i)

#comprehensions

x = {i for i in a}
print(x)

x1 = {i+1 for i in range(10)}
print(x1)

x1 = {i+1 for i in range(20) if i%2 == 0}
print(x1)

x1 = {i+1 for i in range(20) if i%2 == 0 if i%3 == 0}
print(x1)

x1.remove(7)
print(x1)

x1.discard(13)
print(x1)

x1.pop()
print(x1)

a.clear()
print(a)

print(x.issubset(x1))
print(x1.issubset(x))
print(x1.issuperset(x))
print(x.issuperset(x1))
print(x.union(x1))
a.update([10,20,30,40])
b = {10,20,30,40,50}
print(a)
print(a.intersection(b))
print(b.difference(a))
b = {60,70}
print(a.symmetric_difference(b))
b = {40,30}
print(a.intersection_update(b))
print(a.copy())

print(b.difference_update(a))
print(b.symmetric_difference_update(a))
print(a)
print(b)


