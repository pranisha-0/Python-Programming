import numpy as np
I = np.array([
    [8, 3],
    [4, 6]
])

R = np.array([
    [10, 100], 
    [25, 5]
])

V = np.matmul(I, R)
print(f"\n V = IR \n = {V}")