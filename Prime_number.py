'''num=int(input("Enter the number: "))
for i in range(2,num):
    if(num%i==0):
        print(" Not a Prime number")
        break
else:
    print("Prime Number")
'''

#Printing all the prime numbers in the given interval
low=10
upr=59
print("List of all the prime numbers in a given interval: ")
for n in range(low,upr+1):
    if(n>1):
        for i in range(2,n):
            if(n%i==0):
              break
        else:
            print(n,end=" ")




