try:
    a = int(input("ENter num1: "))
    b = int(input("ENter num2: "))
    c = a/b
    print(f"The result is {c:.2f}")

except ZeroDivisionError:
    print("Error: division by zero not allowed.")
except ValueError:
    print("INVALID NUMBER FORMAT.")
