arr=[int(i) for i in input().split()]
print("Given Array is: ",arr)
#Visited_array is used to store the frequencies of elements present in the array.
visited_array=[None]*len(arr)
visited=-1

for i in range(0,len(arr)):
    count=1
    for j in range(i+1,len(arr)):
        if(arr[i]==arr[j]):
            count+=1
            visited_array[j]=visited
    #Store count of each element to visited_array
    if(visited_array[i]!=visited):
        visited_array[i]=count
for i in range(0,len(visited_array)):
    if(visited_array[i]!=visited):
        print("Array Element ",str(arr[i])," comes ",str(visited_array[i]),"times..")


