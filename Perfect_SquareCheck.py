n=int(input("Enter the number: "))
sqr_t=n**0.5
c=int(sqr_t)
if((sqr_t)-c==0):
    print("Yes {0} is a perfect Square..".format(n))
else:
    print("No {0} is not a perfect Square..".format(n))