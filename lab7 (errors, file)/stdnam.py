
with open("students.txt", "w") as f:
    for i in range(1,6):
        name = input(f"ENtr name of std {i}: ")
        f.write(name + "\n")
f.close()
print("File created successfully.\n")

with open("students.txt", "r") as f:
    print("Names of stds: ")
    stds = f.readlines()
    for std in stds:
        print(std.strip())
    print("\nTotal stds: ", len(stds))

