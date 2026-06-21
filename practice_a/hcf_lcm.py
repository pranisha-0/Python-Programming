n1 = int(input("Enter first number: "))
n2 = int(input("Enter second number: "))
if n1 > n2:
    small = n2
else:
    small = n1

for i in range (small, 0, -1):
    if n1%i == 0 and n2%i == 0:
        hcf = i
        break
lcm = (n1*n2)//hcf
print(f"HCF of {n1} and {n2} is {hcf}")
print(f"LCM of {n1} and {n2} is {lcm}")