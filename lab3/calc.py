#calc
n1 = float(input("Enter num1: "))
n2 = float(input("Enter num2:"))
opr  = input("Enter operator: ")

if opr == "+":
    print(f"{n1} + {n2} = {n1+n2: .2f}")
elif opr == "-":
    print(f"{n1} - {n2} = {n1-n2:.2f}")
elif opr == "*":
    print(f"{n1} x {n2} = {n1*n2:.2f}")
elif opr == "/":
    if n2 != 0:
        print(f"{n1} / {n2} = {n1/n2:.2f}")
    else:
        print("Error.")
else:
    print("Invalid operator.")
