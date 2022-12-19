#Method1
'''
print("Enter the elements of an array: ")
arr=[int(i) for i in input().split()]
print("Array is: ",arr)
'''
#Method2
print("Enter the elements of an array: ")
arr=list(map(int,input().split()))
print("Array Elements are: ",arr)