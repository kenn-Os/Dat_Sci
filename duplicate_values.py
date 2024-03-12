from pandas import Series, DataFrame

# Check for duplicate values in a series
se = Series([100, 20, 300], index=['a', 'b', 'c'])
print(se.index.is_unique)

# Check for duplicate index in dataframe
data = {
    'Speed': [80, 100, 120],
    'Temp': [27, 12, 38],
    'Humidity': [1200, 1890, 2300]
}
frame = DataFrame(data)
print(frame)
print('\n')

# Let us reindex and check for duplicate index
frame = frame.reindex([0, 2, 2, 1])
print(frame)
print(frame.index.is_unique)