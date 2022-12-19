#Method1
'''
arr=[int(i) for i in input("Enter Array Elements: ").split()]
print("Elements at Even position count: ")
#For Odd Position Elements just use...."range(0,len(arr),2)"
for i in range(1,len(arr),2):
    print(arr[i],end=" ")
'''
#Method2
arr=[int(i) for i in input("Enter Array Elements: ").split()]
print("Elements at Even position count: ")
for i in range(0,len(arr)):
    if(i%2==0):
      print(arr[i],end=" ")