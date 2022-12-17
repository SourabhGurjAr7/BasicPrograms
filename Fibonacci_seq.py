#without Recursion

a=0
b=1
count=0
terms=int(input("Enter the terms you want to print: "))
if(terms==0):
  print("Not a valid input")
elif(terms==1):
  print(a)
else:

  while(count<terms):
    print(a,end=" ")
    c=a+b
    a=b
    b=c
    count+=1
