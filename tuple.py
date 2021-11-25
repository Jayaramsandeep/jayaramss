l = [1,2,5,7,4,3,111,10,11,15]
for i in range(len(l)):
    for j in range(i+1,len(l)):
        if l[i]>l[j]:
            l[i],l[j] = l[j],l[i]
print(l)
