import numpy as np
a = np.array([
    [1, 2, 3], 
    [4, 5, 6],
    [0, 9, 10]
])

b = np.array([
    [21, 38, 21],
    [15, 39, 19],
    [2, 7, 0]
])

sub = a-b
print(f"\nMatA - MatB = \n{sub}")
mul = a*b
print(f"\nmatA * matB (elementwise) = \n{mul}")

mat_mul = np.matmul(a, b)
print(f"\nmatA * matB = \n{mat_mul}")