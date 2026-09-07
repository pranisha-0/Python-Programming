import numpy as np

print(np.__version__)
#1D array and indexing slicing
a = np.array([1, 2, 3, 4, 6])
print(a[1])
print(a[0:4])
print(a[3:])
print(a[:])

#2D array and indexing slicing
b = np.array([
    [1, 2, 3],
    [4, 5, 6]
])
print(b[1, 2]) 
#2D array ko indexing b[row, column] bata garinxa
print(b[:2, 1:2])

#print(np.zeros(3, 4))

c = a
c[0] = 100
print(c[0])
print(a)
d = c.copy()
print(d)

a[a>10] = 7
print(a)