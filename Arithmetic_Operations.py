n=int(input("Enter First Value: "))
m=int(input("Enter Second Value: "))
def add(n,m):
    return n+m
def sub(n,m):
    return n-m
def mul(n,m):
    return n*m
def div(n,m):
    return n/m
print("Addition of numbers {0} and {1} is {2}".format(n,m,add(n,m)))
print(abs(sub(n,m)))
print(mul(n,m))
print(div(n,m))


