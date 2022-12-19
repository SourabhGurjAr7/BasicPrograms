
print("Enter the elements of an array: ")
arr=[int(i) for i in input().split()]
#Create another array arr1 with size of arr
arr1=[None]*len(arr)
for i in range(0,len(arr)):
    arr1[i]=arr[i]
print("Before copying the elements: ")

for i in range(0,len(arr)):
    print(arr[i],end=" ")
print("\n")
print("After copying the elements of arr1 are : ")
for i in range(0,len(arr1)):
    print(arr1[i],end=" ")

