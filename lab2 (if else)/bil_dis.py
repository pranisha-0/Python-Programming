amt = float(input("Enter the amount: "))
if amt > 5000:
    amt = amt - (amt * 0.1)
    print(f"The amount after discount is {amt}")
else:
    print(f"The amount is {amt}")