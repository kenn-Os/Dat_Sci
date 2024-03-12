from pandas import DataFrame, Series

obj = Series([100, 200, 300], index=['c', 'a', 'b'])
print(obj)
print('\n')

# Reindex a Series
obj = obj.reindex(['a', 'b', 'c'])
print(obj)
print('\n')

# Reindex a DataFrame
data = {
    'Name': ['Barner', 'Steve', 'Scarlet'],
    'Age': [32, 33, 40],
    'Salary': [5000, 4000, 7000]
}

frame = DataFrame(data)
print(frame)
print('\n')

# Reindex Rows
frame = frame.reindex([0, 2, 1])
print(frame)
print('\n')

# Reindexing column
frame = frame.reindex(columns=['Name', 'Age', 'Salary'])
print(frame)

# Deleting rows and columns from a dataframe
# Delete a row
frame2 = frame.drop(2)
print(frame2)
print('\n')

# Delete a column
frame3 = frame.drop('Age', axis=1)
print(frame3)
print('\n')