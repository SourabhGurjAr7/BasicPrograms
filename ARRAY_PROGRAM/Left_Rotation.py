arr=[int(i) for i in input("Enter Array Elements: ").split()]
print("Given Array is: ",arr)

print("Positions we want to rotate our Array to  : ")
n=int(input())
for i in range(0,n):
    first=arr[0]
    for j in range(0,len(arr)-1):
        arr[j]=arr[j+1]
    arr[len(arr)-1]=first
print("Array after left Rotation is :")
for i in range(0,len(arr)):
    print(arr[i],end=" ")
