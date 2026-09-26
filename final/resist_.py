resistance_list = []
for i in range(10):
    r = input(f"Enter value of resistor {i+1}: ")
    resistance_list.append(float(r))

print(f"the resistance are: {resistance_list}")
total = sum(resistance_list)
avg = total/len(resistance_list)
print(f"the total resistance is: {total:.2f}")
print(f"the average is: {avg:.2f}")