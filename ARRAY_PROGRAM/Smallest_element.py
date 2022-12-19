arr=[int(i) for i in input("Enter array elements: ").split()]
smallest=arr[0]
for i in range(1,len(arr)):
    if(arr[i]<smallest):
        smallest=arr[i]
print("Smallest element in an Array: ",smallest)