def fact(n):
    if n == 0 or n == 1:
        return n
    else:
        return n * fact(n-1)
n = int(input("enter a number: "))
if n<0:
    print("invalid input")
else:
    print(f"The factorial of {n} is {fact(n)}")
