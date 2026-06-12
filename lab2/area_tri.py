#Write a program to input three sides of a triangle and find the area if these sides form a triangle.
a = float(input("Enter side1: "))
b = float(input("ENter side2: "))
c = float(input("ENter side3: "))
if a>b:
    if a>c:
        big = a
    else:
        big = c
else: 
    if b>c:
        big = b
    else:
        big  = c
if big < a+b+c-big:
    s = (a+b+c)/2
    area = (s*(s-a)*(s-b)*(s-c))**0.5
    print(f"The area of the triangle is {area:.2f}")
else:
    print("The sides do not form a triangle.")


