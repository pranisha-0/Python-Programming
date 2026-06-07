s1 = float(input("Enter markof subject1: "))
s2 = float(input("Enter markof subject2: "))
s3 = float(input("Enter markof subject3: "))
s4 = float(input("Enter markof subject4: "))
s5 = float(input("Enter markof subject5: "))
total = s1 + s2 + s3 + s4 + s5
avg = (total) /5
per = ((total) / 500) * 100
print(f"Total marks: {total:.3f}. \nAverage Marks: {avg:.3f}. \nPercentage: {per:.3f}%. \n")