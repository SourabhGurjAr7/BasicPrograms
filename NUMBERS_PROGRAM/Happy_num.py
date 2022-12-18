#Check whether number is Happy Number or not...
'''
def Is_Happy(n):
    rem=sum=0
    while(n!=0):
        rem=n%10
        sum=sum+rem**2
        n=n//10
    return sum
n=int(input("Enter the number to check: "))
result=n
while(result!=1 and result!=4):
    result=Is_Happy(result)

if(result==1):
    print(n,"is a Happy Number..")
else:
    print(n, "isn't a Happy Number..")
'''

#Print all the Happy Numbers in given Range

def Is_Happy(n):
    rem=sum=0
    while(n!=0):
        rem=n%10
        sum=sum+rem**2
        n=n//10
    return sum

for i in range(1,100):
    result=i
    while(result!=1 and result!=4):
        result=Is_Happy(result)
    if(result==1):
        print(i,end=" ")





