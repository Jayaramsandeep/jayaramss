def solutions(S, T):
    pass
    S = 'eat'
    T = S
    T ='t'+S
    print("S = " +S)
    print("T = " + T)

    S = 'eats'
    print("S = " + S)
    T = S
    if T == S:
        print('T = eat')

    s = 'abcedf'
    S = list(s)
    s = str(S)
    print('S = '+ s)
    T = S
    t = list(T)
    t[2] = 'd'
    t[4] = 'c'
    T = str(t)
    print('T = '+T)

    S = "sandeep"
    print("S = " + S)
    T = S

    if S == T:
        print('T = ' + T)

    def sol(S, T):
        S = 'O'
        T = S+'dd'
        C = "Impossible"
        return C
    res = sol("", "")
    print(res)
solutions('', '')

for N in range(1,100,3):
    print(N,end=" ")
print()
for M in range(1,100,3):
    print(M, end=" ")
print()


S= 'eat'
for T in S:
    if T == S:
        print(T+'s')




