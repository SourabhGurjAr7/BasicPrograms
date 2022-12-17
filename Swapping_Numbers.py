a=int(input("enter First Number: "))
b=int(input("enter Second Number: "))
print("Numbers before swapping are {0} and {1}".format(a,b))
t=a
a=b
b=t

#Another way to swap using comma operator
'''
a,b=b,a'''

#Using + and - operator
'''
a=a+b
b=a-b
a=a-b
'''
print("After Swapping numbers are {0} and {1}".format(a,b))
