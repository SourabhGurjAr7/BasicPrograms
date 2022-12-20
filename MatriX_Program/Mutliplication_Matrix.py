r=int(input("Enter row: "))
c=int(input("Enter column: "))
mat1=[[int(input())for i in range(r)] for j in range(c)]
print("1st Matrix is: ",mat1)

r1=int(input("Enter row: "))
c1=int(input("Enter column: "))
mat2=[[int(input())for i in range(r1)] for j in range(c1)]
print("2nd Matrix is: ",mat2)
#Matrix with Zeros
r2=int(input("Enter row: "))
c2=int(input("Enter column: "))
mutli_mat=[[int(input())for i in range(r2)] for j in range(c2)]
print("Empty Matrix is: ",mutli_mat)

print("Multiplication of Matrix: ")
for i in range(len(mat1)): #row of mat1
    for j in range(len(mat2[0])): #column of mat2
        for k in range(len(mat2)): #row of mat2
            mutli_mat[i][j]+=mat1[i][k]*mat2[k][j]
for r in mutli_mat:
    print(r)