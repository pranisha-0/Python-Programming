A = []
B = []
C = []
D = []

n = int(input("Enter order of matrix: "))

print("\nInput of A: ")
for i in range(n):
    row = []
    print("\n")
    for j in range(n):
        a = int(input(f"Enter element of A[{i}][{j}]: "))
        row.append(a)
    A.append(row)

print("\nInput of B: ")
for i in range(n):
    row = []
    print("\n")
    for j in range(n):
        b = int(input(f"Enter element of B[{i}][{j}]: "))
        row.append(b)
    B.append(row)

print("\n AxB: ")
for i in range(n):
    row = []
    for j in range(n):
        total = 0
        for k in range(n):
            total += A[i][k] * B[k][j]
        row.append(total)
    C.append(row)

for r in C:
    print(r)