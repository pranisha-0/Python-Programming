import numpy as np

print(np.__version__) #numpy ko version check garna
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

c = a #copies a to c but dependntly i.e if c changes, a will also change
c[0] = 100
print(c[0])
print(a)
d = c.copy() #copies array c to d independently i.e if d changes c wont change
print(d)

a[a>10] = 7 #chhanges every number in the array which is greater than 10 to 7
print(a) 

b[1, 1] = 50
print(b)

print("\n")
p = np.array([[1, 2, 3], [4, 5, 6]])
q = np.array([[6, 8, 3], [9, 0, 7], [4, 3, 7]])
t = np.matmul(p, q)#np.dot(p, q)
print(t)