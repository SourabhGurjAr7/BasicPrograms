#Check whether number is Disarium or not
'''
def Cal_Length(n):
    length=0
    while(n!=0):
        length=length+1
        n=n//10
    return length
num=int(input("Enter the number to check: "))
rem=sum=0
n=num
len=Cal_Length(num)
while(num>0):
        rem=num%10
        sum=sum+int(rem**len)
        num=num//10
        len=len-1

if(sum==n):
    print("It is a Disarium number")
else:
    print("Not a Disarium number")

'''

#Printing All Disarium numbers in a given range

def Cal_Length(n):
    length=0
    while(n!=0):
        length=length+1
        n=n//10
    return length

def Cal_Sum(num):
    rem=sum=0
    len = Cal_Length(num)
    while(num>0):
        rem=num%10
        sum=sum+int(rem**len)
        num=num//10
        len=len-1
    return sum
result=0
for i in range(1,250 ):
    result=Cal_Sum(i)
    if(result==i):
        print(i,end=" ")

