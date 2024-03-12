import numpy as np

a = np.array({
  [1, 2, 3],
  [4, 5, 6]
})

# ndim: means how many indexes you need to access an element in the numpy

print(a.ndim)

# accessing element itself

print(a[1][2])
print(a[0][1])

b = np.array([
  [[1, 2, 3], [4, 5, 6], [7, 8, 9]],
  [[-1, 2, 3], [4, 5, 6], [7, 8, 9]],
])

print('\n')

print(b[1, 1, 2])
print(b.ndim)

print('\n')

# shape: this method returns how a numpy is presented

print(b.shape)
print('\n')

# size: this is the total amount of elements in the numpy
print(b.size)
