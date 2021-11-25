# for empty dictionary

a = dict()
print(type(a))

b = {10: 1, 20: 30, 40: 50}
print(b)

#accessing dictionary
print(b[10])

#upadate
b[0]="sandeep"

#reassing dictionary
b[10]= "jayaram"
print(b)

#deleting dictionary
del(b[0])
print(b)

#dictionary comprehension

c ={i:i for i in range(1,10)}
print(c)

c ={i:i**2 for i in range(1,10)}
print(c)

c ={i:i**2 for i in range(1,100,5) if i%3 == 0 }
print(c)

#multidimensional dictionary

d = {10:{10:10,20:20,30:30},20:{i:i for i in range(1,5)},'multi':{i:i**2 for i in range(1,10,2) if i%3 == 0 }}
print(d)
print(d[10])
print(d[20])
print(d['multi'])

a.clear()
print(a)
a = b.copy()
print(a)
print(b.items())
print(b.values())
print(b.get(10))
print(b.pop(40))
print(b.popitem())
print(b.keys())
print(b.setdefault(20))
print(b)
print(a)
