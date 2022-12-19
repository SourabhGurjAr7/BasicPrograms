arr=[int(i) for i in input("Enter array elements: ").split()]
sum=0
for i in range(0,len(arr)):
    sum=sum+arr[i]
print("Sum of Array Elements is: ",sum)