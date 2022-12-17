#Sum of first n natural numbers.

n=int(input("Enter the number: "))
sum=0
for i in range(1,n+1):
    sum=sum+i
print("Sum of {0} natural numbers is {1}".format(n,sum))
