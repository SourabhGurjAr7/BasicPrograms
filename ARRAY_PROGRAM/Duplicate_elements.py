print("Enter the elements of an array: ")
arr=[int(i) for i in input().split()]
print(arr)
print("Duplicate elements are: ")
for i in range(0,len(arr)):
    for j in range(i+1,len(arr)):
        if(arr[i]==arr[j]):
          print(arr[j],end=" ")