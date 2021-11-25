"""set of characters are placed in the  ("" or '') it shouled be called as string """

#empty string

a = str()
print(type(a))

#creating
a = "jayaram"

#accessigning
print(a[0])

#slicing

print(a[:])
print(a[2:])
print(a[1:3])

#single double triple quotes

b = "jayaram's"
print(b)
c = 'sandeep"s'
print(c)

#formate method

d = "{0} is a hero,{1} is a god".format('jayaram','jayaram')

print(d)

print(max(a))
print(min(a))
print(len(a))
print('j' in a)

for i in a:
    print(i,end=" ")

#bulit in methods

print(a.capitalize())
print(a.isalnum())
print(a.isalpha())
print(a.endswith('m'))
print(a.startswith('j'))
print(a.isdigit())
print(a.isdecimal())
print(a.find('j'))
print(a.rfind('j'))
print(a.ljust(10))
print(a.rjust(10))
print(a.index('j'))
print(a.rindex('j'))
print(a.replace('j','J'))
print(a.split('j'))
print(a.center(10))
print(a.rsplit('j'))
print(a.istitle())
print(a.strip())
print(a.rstrip('j'))
print(a.lstrip('j'))
print(a.lower())
print(a.islower())
print(a.upper())
print(a.isupper())
"""still have more on this type commands see the books and find that """