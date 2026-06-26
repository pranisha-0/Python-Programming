n = int(input("Enter num of elements: "))
num_list = []
for i in range(0, n):
    num = int(input(f"Enter number {i+1}: "))
    num_list.append(num)
sum = 0
for i in num_list:
    sum = sum +i
print(f"The sum of the list is {sum}")
    
