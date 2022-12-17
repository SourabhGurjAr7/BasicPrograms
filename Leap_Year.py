yr=int(input("Enter the Year to check : "))
if((yr%400==0) or (yr%4==0) and (yr%100!=0) ):
    print("Leap Year")
else:
    print("Not a Leap Year")