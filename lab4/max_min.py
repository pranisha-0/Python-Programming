n = int(input("Enter no of elements: "))
num_list = []

for i in range(n):
    num = int(input(f"Enter number {i+1}: "))
    num_list.append(num)

max = num_list[0]

for i in num_list:
    if i > max:
        max = i

min = num_list[0]

for i in num_list:
    if i < min:
        min = i

print(f"The largest number is {max}")
print(f"The smallest number is {min}")