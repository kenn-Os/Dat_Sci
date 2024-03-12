from pandas import Series

# Creating Series
se = Series([1, 3, 5, 7, 9])
print(se)
print('\n')

# Accessing elements
print(se[2])
print('\n')

# Creating a series with custom index/position
se2 = Series([100, 200, 300], index=['a', 'b', 'c'])
print(se2)
# Access element
print(se2['a'])
print('\n')

# Converting dictionary to series
salary = {
    'John': 3000,
    'Tim': 4500,
    'Rob': 5000
}
print(salary)
se3 = Series(salary)
print(se3)

# Access elements
print(se3['Rob'])
