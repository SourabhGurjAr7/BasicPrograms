#LCM of number

n1=int(input("Enter first number: "))
n2=int(input("Enter second number: "))
for m in range(1,n1*n2+1):
    if(m%n1==0 and m%n2==0):
      print("LCM of a {0} and {1} is {2}".format(n1,n2,m))
      break