n = int(input("Enter a number: "))
print("\n ")
print(f"The multiplication table of {n} is:")

i=1
while(i<=10):
    prod = n*i
    print(f"{n} x {i} = {prod}")
    i = i+1