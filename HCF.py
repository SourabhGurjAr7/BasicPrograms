#HCF of 2 Numbers

a=int(input("Enter 1st number:"))
b=int(input("Enter 2nd number: "))
t1=a
t2=b
while(a%b!=0):
    rem=a%b
    a=b
    b=rem
gcd=b
print("HCF of {0} and {1} is {2}".format(t1,t2,gcd))