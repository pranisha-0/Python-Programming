a = int(input("Enter coeff of x^2: "))
b = int(input("Enter coeff of x: "))
c = int(input("Enter value of c: "))

d = b**2 - 4*a*c
if d == 0:
    root = -b/(2*a)
    print("The roots are real and equal. ")
    print(f"The root is {root}. ")
elif d>0:
    root1 = (-b + (d**0.5))/(2*a)
    root2 = (-b - (d**0.5))/(2*a)
    print("The roots are real and unequal.")
    print(f"The roots are {root1} and {root2}. ")
else:
    print("The roots are imaginary.")
 