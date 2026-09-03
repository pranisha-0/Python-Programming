try:
    n = int(input("Enter a number: "))
    p = 1
    if n == 1 or n == 0:
        print("The factorial of", n, "is 1")
    else:
        for i in range(1, n+1):
            p *= i
        print("The factorial of", n, "is", p)
except Exception as e:
    print("Error: ", e) s
