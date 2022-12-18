#Check whether number is Harshad or not..
'''
def Harshad_Num(n):
  sum=0
  while(n>0):
    rem=n%10
    sum=sum+rem
    n=n//10
  return sum

n=int(input("Enter the number: "))
if(n%Harshad_Num(n)==0):
  print(n,"--Yes! It is a Harshad Number")
else:
  print(n,"--No! It isn't a Harshad Number")

'''
#Print all the Harshad Numbers in a given Range..

def Harshad_Num(n):
  sum=0
  while(n>0):
    rem=n%10
    sum=sum+rem
    n=n//10
  return sum
print("List of all the Harshad Numbers in given Range: ")
for i in range(1,110):
    res=Harshad_Num(i)
    if(i%res==0):
        print(i,end=" ")
