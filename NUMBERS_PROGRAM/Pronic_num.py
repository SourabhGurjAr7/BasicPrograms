#Check whether number is Pronic or not....12=3*4
'''
def Check_Pronic(n):
    for i in range(1,n):
        if(n==i*(i+1)):
            print("Yes It is A Pronic Number")
            break
    else:
        print("No it is not a Pronic number")
n=int(input("Enter the Number: "))
Check_Pronic(n)
'''
#print all the pronic numbers within a given range

def Check_Pronic(n):
    for i in range(1,n):
        if(n==i*(i+1)):
            return n
print("List of all the Pronic Numbers in a given range: ")
for i in range(0,500):
    if(i==Check_Pronic(i)):
        print(i,end=" ")
