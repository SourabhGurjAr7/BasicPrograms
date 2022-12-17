#print all the pallindrome numbers within a given range

print("Pallindrome numbers within a given are: ")
for n in range(100,200):
 rev = 0
 temp = n
 while(n>0):
    rem=n%10
    rev=rev*10+rem
    n=n//10
    if(temp==rev):
     print((temp),end="  ")


