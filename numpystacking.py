import numpy as np

a = np.round(10 * np.random.rand(2, 3))
print(a)
print('\n')

# Broadcasting
print(a * 3)
print('\n')

# Horizontal Stacking
b = np.round(10 * np.random.rand(2, 3))
print(b)
c = (np.hstack((a, b)))
print(c)
print('\n')

# Vertical Stacking
b = np.round(10 * np.random.rand(2, 3))
print(b)
c = (np.vstack((a, b)))
print(c)
print('\n')

# Sorting
e = np.random.permutation(np.arange(10))
print(e)
print(np.sort(e))

# reversed 
e = e[::-1]
print(e)




