def jay():
    print("jayaram is hero")
jay()


def jay(a):
    print(a+ "hero")
jay("jayaram is ")

def jay(a,b):
    print(a+"hero"+b)
jay("jayaram is ",",jayaram is god")

def jay(c):
    return c
r = jay(10)
print(r)

def jay(a,b):
    c = a+b
    return c
r = jay(10,20)
print(r)

def jay(*san):
    print(san)
jay(10,20,30,40,50,60,70)

a =lambda a,b,c:a*b*c
print(a(10,20,30))

def rec(n):
    if n == 0 or n == 1:
        return 1
    else:
        return n*rec(n-1)
print(rec(4))
