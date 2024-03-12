from pandas import Series, DataFrame

se = Series([2, 2, 19, 15])
se2 = Series([12, 37, 40, 55])

print(se + se2)
print('\n')

se3 = Series([2, 7, 10, 15])
se4 = Series([12, 37, 40, 55, 67, 88])
print(se3 + se4)
print('\n')

data = {
    'Speed': [100, 120, 180],
    'Temp': [30, 70, 87]
}

data2 = {
    'Speed': [100, 120, 180],
    'Temp': [30, 70, 87],
    'Humidity': [1300, 1700, 2400]
}

frame = DataFrame(data)
frame2 = DataFrame(data2)

print(frame + frame2)
print("\n")

# add series and dataframe
se5 = Series([100, 400], index=['Speed', 'Temp'])
print(se5 + frame)
print('\n')

print(se5 + frame2)
print('\n')

# some other calculations
print(frame2)
print('\n')

# summation of columns
print(frame2.sum())

# summation of rows
print(frame2.sum(axis=1))
print('\n')

# maximum value
print(frame2.max())
print(frame2.idxmax())
print('\n')

# minimum value
print(frame2.min())
print(frame2.idxmin())
print('\n')