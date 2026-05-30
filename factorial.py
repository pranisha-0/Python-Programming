num = int(input("enter a positive number: "))
if num<0:
    print("I SAID POSITIVE NUMBER")
else: 
    fact = 1
    for i in range(1, num+1):
        fact *= i
    print("the factorial of ", num, "is: ", fact)