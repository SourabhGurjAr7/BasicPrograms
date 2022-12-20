#If Matrix of dimensions....n*m
row=int(input("Enter the number of rows: "))
column=int(input("Enter the number of columns: "))
matr=[[int(input())for i in range(row)]for j in range(column)]

print(matr)
r1=int(input("Enter the number of rows : "))
c1=int(input("Enter the number of columns: "))
transpose_Matrix=[[int(input()) for i in range(r1)] for j in range(c1)]
#Empty matrix must be of dimensions...m*n
print(transpose_Matrix)
for i in range(len(matr)):
    for j in range(len(matr[0])):
        transpose_Matrix[j][i]=matr[i][j]
print("Transposed Matrix is : ")
for r in transpose_Matrix:
    print(r)