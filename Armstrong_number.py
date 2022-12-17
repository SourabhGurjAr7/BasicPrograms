'''n=int(input("Enter the number: "))
temp=n
sum=0
while(n>0):
    rem=n%10
    sum=sum+rem**3
    n=n//10
if(temp==sum):
    print("Yes!..It is Armstrong number.")
else:
    print("No!..It's not Armstrong number.")
'''

#Armstrong Numbers in given interval

low=int(input("Enter lower value: "))
upr=int(input("Enter upper Value: "))
print("All the Armstrong Numbers in given interval are: ")
for n in range(low,upr+1):
    temp = n
    sum = 0
    while(n>0):
     rem=n%10
     sum=sum+rem**3
     n=n//10
     if(temp==sum):

       print(temp,end=" ")

