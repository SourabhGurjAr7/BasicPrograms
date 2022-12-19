#Method1
'''
arr=list(map(int,input("Enter the Array Elements: ").split()))
print(arr)
for i in reversed(range(0,len(arr))):
    print(arr[i],end=",")
'''
#Method2
arr=list(map(int,input("Enter the Array Elements: ").split()))
# start = list's size
# stop = -1
# step = -1
print(arr)
for i in range(len(arr)-1,-1,-1):
    print(arr[i],end=",")