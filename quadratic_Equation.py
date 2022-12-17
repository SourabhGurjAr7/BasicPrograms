a = int(input('Enter first value: '))
b = int(input('Enter second value: '))
c = int(input('Enter third value: '))
if(b*b<4*a*c):
    print("Roots are not real(COMPLEX): ")
    root1=-b/(2*a),' +i',(abs(b*b-4*a*c))**0.5
    root2=-b/(2*a),'-i',(abs(b*b-4*a*c))**0.5
    print(root1)
    print(root2)
elif(b*b==4*a*c):
    print("Roots are  same and real: ")
    root3=-b/2*a
    print(root3)
else:
    print("Real Roots: ")
    root4=(-b+(b*b-4*a*c)**0.5)/2*a
    root5=(-b-(b*b-4*a*c)**0.5)/2*a
    print(root4)
    print(root5)

