import numpy as np

a = np.arange(10)
print(a)
print('\n')

# creating the slice object
s = slice(2, 7, 2)
print(a[s])
print('\n')
# another method
b = a[2:7:2]
print(b)
print('\n')

# slice from a position to the end
print(a[2:])

c = np.array([[1, 2, 3], [4, 5, 6], [7, 8, 9]])
print(c)
print('\n')

# slicing
d = c[[0, 1, 2], [0, 1, 0]]
print(b)
print('\n')

