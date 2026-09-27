#qs = 2x+3y=84      x-y=2 solve
import numpy as np
A = np.array([[2, 3], [1, -1]])
B = np.array([84, 2])

soln = np.linalg.solve(A, B)
print(f"x = {soln[0]:.2f}")
print(f"y = {soln[1]:.2f}")


#qs: 2x+3y=12       4x-5y=-2

C = np.array([[2, 3], [4, -5]])
D = np.array([12, -2])

result = np.linalg.solve(C, D.T)
print(f"x = {result[0]:.2f}")
print(f"y = {result[1]:.2f}")