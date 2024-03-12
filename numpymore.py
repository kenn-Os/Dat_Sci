import numpy as np

# arange: used to fill up a numpy array with a specified range.

a = np.arange(100)
print(a)
print('\n')

# setting a range

b = np.arange(0, 101, 2)
print(b)
print('\n')

#  random.permutation: it rearranges a number in a random format
c = np.random.permutation(np.arange(10))
print(c)
print('\n')

#  random.rand function : generates a numpy of floating numbers based on a given dimension
d = np.random.rand(2, 3)
print(d)
print('\n')

e = np.random.rand(2, 3, 4, 2)
print(e)
print('\n')

# {
  # [[0000], [0000], [0000]],
  # [[0000], [0000], [0000]]
# }

# argwhere: getting the index of an element
n = np.arange(15, 30)
print(n)
idx = np.argwhere(n == 10)[0][0]
print(idx)
print('\n')

# reshape: changes the dimension of a numpy
j = np.arange(100).reshape(4, 5, 5)
print(j)
print('\n')

# changing an element
n[idx] = -23
print(n)
print('\n')

# getting elements using a comparison operator
m = np.arange(100)
o = m(m < 40)
print(o)
print('\n')

# looping through a numpy
p = np.arange(0, 60, 5).reshape(3, 4)
print(p)
print('\n')

# iterate
for x in np.nditer(p):
  print(x)

