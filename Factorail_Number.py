fact=1
number=int(input("Factorial of "))
if(number<0):
    print("Inavlid Value")
elif(number==0):
    print("1")
else:
    for i in range(1,number+1):
       fact=fact*i
    print("Answer is: ",fact)