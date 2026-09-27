#qs = 2x+3y=84      x-y=2 solve
import numpy as np
A = np.array([[2, 3], [1, -1]])
B = np.array([84, 2])

soln = np.linalg.solve(A, B)
print(f"x = {soln[0]:.2f}")
print(f"y = {soln[1]:.2f}")