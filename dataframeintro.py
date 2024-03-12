from pandas import DataFrame

data = {
    'Name': ['John', 'Smith', 'Patel'],
    'Age': [30, 45, 25],
    'Gender': ['Male', 'Female', 'Female'],
    'Salary': [4500, 2300, 5600]
}

frame = DataFrame(data)
print(frame)
print('\n')

# Changing Column Sequence
new_frame = DataFrame(data, columns=['Age', 'Name', 'Gender', 'Salary'])
print(new_frame)
print('\n')

# Adding more columns to the table, but the values will be NAN
new_frame2 = DataFrame(data, columns=['Age', 'Name', 'Gender', 'Salary', 'Department'])
print(new_frame2)
print('\n')

# Accessing Elements
# Retrieve data as a series (a particular column)
print(new_frame['Salary'])
print('\n')

# Retrieve data from row
print(new_frame.loc[2])
print('\n')

# Modifying a dataframe
# Editing NaN column
new_frame2['Gender'] = 'Male'
print(new_frame2)
print('\n')

new_frame2['Department'] = 'Sales'
print(new_frame2)
print('\n')

# Modifying Column not present in table
new_frame2['Education'] = 'MsC'
print(new_frame2)
print('\n')

# Transposing
# Turning rows into columns and vice versa
new_frame = new_frame.T
print(new_frame)