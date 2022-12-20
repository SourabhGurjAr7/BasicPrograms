arr=list(map(int,input("Enter the Values: ").split()))
print("Original Array is: ",arr)
print("Positions to which we want to rotate our array: ")
n=int(input())
for i in range(0,n):
    last=arr[len(arr)-1]
    #For Right Rotation,we have to traverse an array in reverse order...
    #for j in range(len(arr)-1,-1,-1):
    #    OR
    for j in reversed(range(0,len(arr))):
        arr[j]=arr[j-1]
    arr[0]=last
print("After Right Roatation Array will become: ")
for i in range(0,len(arr)):
    print(arr[i],end=" ")