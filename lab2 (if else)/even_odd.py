#Write a Python program to input a number and determine whether it is even or odd using the modulus (%) operator.

n = int(input("Enter a nmber: "))
if n % 2 == 0:
    print(("The number is even."))
else:
    print("The number is odd.")