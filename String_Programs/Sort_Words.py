#Method1

str=input("Enter the String to Sort: ")
#We have to first sort our into same Case Alphabet(either lowerCase or UpperCase)
c=str.lower()
str1=list(c)
print(str1)
for i in range(0,len(str1)):
    for j in range(i+1,len(str1)):
        #Basic Swapping method
        if(str1[i]>str1[j]):
            temp=str1[i]
            str1[i]=str1[j]
            str1[j]=temp
print("Sorted List is: ")
print(str1)

'''
#Methdo2

str="Hello I Am Sourabh Panwar"
#To sort a string ,we first have to split() it....But in case of List input we don't have to use split() method
words=str.split()
words.sort()
for i in words:
    print(i,end=" ")
    
#Method3

Lst=["George","Kristen","Kuno","Adam"]
Lst.sort()
print("Sorted list : ")
for i in Lst:
    print(i,end=" ")
'''

