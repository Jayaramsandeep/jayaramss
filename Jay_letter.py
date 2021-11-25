str = "JAY"

J = [[" " for i in range(5)] for j in range(5)]
A = [[" " for i in range(5)] for j in range(5)]

#J
for row in range(5):
    for col in range(5):
        if row == 0 and (col != 0 and col != 1) or col == 4 or row == 4 and (col != 0) or  row == 3 and (col != 0 or col != 2 or col != 3 or col != 4):
            J[row][col] = '*'
for row in range(5):
    for col in range(5):
        if col == row == 2 :
            J[row][col] = '*'
for i in range(5):
    for j in range(5):
        print(J[i][j],end=" ")
    print(end=" ")
    for j in range(5):
        print(A[i][j],end=" ")
    print()
