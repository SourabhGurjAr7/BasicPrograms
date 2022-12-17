def fibo(n):
    if(n<0):
        return "Invalid Input"
    elif(n==0):
        return 0
    elif(n==1):
        return 1
    else:
        return (fibo(n-1)+fibo(n-2))
terms=int(input("Enter the terms of Fibonacci series to print: "))

for i in range(terms):
   print(fibo(i),end=" ")