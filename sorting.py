from pandas import DataFrame, Series

se = Series([3, 7, 1, 4, 7, 2], index=[2, 7, 3, 5, 9, 1])
print(se)
print('\n')

# Sorting
print(se.sort_index())
print('\n')

data = {
    'Speed': [80, 100, 120],
    'Temp': [27, 12, 38],
    'Humidity': [1200, 1890, 2300]
}
frame = DataFrame(data)
print(frame)
print('\n')

# Reindexing
frame = frame.reindex([2, 1, 0,])
print(frame)
print('\n')

# Sorting the rows
print(frame.sort_index())
print('\n')

# Sorting the column
print(frame.sort_index(axis=1))
print('\n')

# Sorting in descending order
print(frame.sort_index(axis=1, ascending=False))
print('\n')

# Sorting series by values
se2 = Series([1400, 1200, 3100], index=['Speed', 'Temp', 'Humidity'])
print(se2)
print('\n')
print(se2.sort_values())
print('\n')

# Sorting DataFrame by values
print(frame)
print('\n')
print(frame.sort_values(by='Humidity'))