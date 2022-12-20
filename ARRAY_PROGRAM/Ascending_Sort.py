arr=list(map(int,input("Enter the Values: ").split()))
print("Original Array is: ",arr)
temp=0
for i in range(0,len(arr)):
    for j in range(i+1,len(arr)):
        if(arr[j]<arr[i]):
            #Apply Swapping logic
           temp=arr[i]
           arr[i]=arr[j]
           arr[j]=temp
print("Ascending order of an Array : ")
for k in range(0,len(arr)):
    print(arr[k],end=" ")