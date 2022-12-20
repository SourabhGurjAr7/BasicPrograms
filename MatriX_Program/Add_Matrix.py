#For addition of 2 matrixes ,the dimensions of both must be same

row=int(input("Enter the number of rows: "))
column=int(input("Enter the number of columns: "))
x=[[int(input())for i in range(row)]for j in range(column)]
print("1st Matrix: ")
print(x)

row1=int(input("Enter the number of rows: "))
column1=int(input("Enter the number of columns: "))
Y=[[int(input())for i in range(row1)]for j in range(column1)]
print("2nd Matrix: ")
print(Y)

row2=int(input("Enter the number of rows: "))
column2=int(input("Enter the number of columns: "))
result=[[int(input())for i in range(row2)]for j in range(column2)]
print(result)

for i in range(len(x)):
    for j in range(len(x[0])):
        result[i][j]=x[i][j]+Y[i][j]
print("Addition of Matrix : ")
for r in result:
    print(r)
