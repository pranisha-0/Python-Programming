with open("students.txt", "a") as f:
    for i in range (4):
        name = input(f"Enter name of student {i+6}: ")
        f.write(name)
        f.write("\n")
f.close()
print("\n ---FILE UPDATED SUCCESSFULLY--- \n")
with open("students.txt", "r") as f:
    print("UPDATED FILE: ")
    std = f.read() #f.readlines() is also fine but it reads as a list so we use loop to print
    print(std)