'''with open("students.txt", "r") as f:
    c = f.read(5)
    print(c)'''

lines = ["First line\n", "Second line\n", "Third line\n"]
with open("output.txt", "w") as file:
    file.writelines(lines)

print("FILE CREATED.")

with open("output.txt", "r") as f:
    c = f.read()
    print(c)