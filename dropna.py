import numpy as np
from pandas import DataFrame, Series

# Series NaN dropping
se = Series([1, 2, 3, 4, np.nan], index=['a', 'b', 'c', 'd', 'e'])
print(se)
print('\n')

# Filtering
se = se.dropna()
print(se)
print('\n')

# Dataframe NaN dropping
data = {
    'Speed': [80, 100, 120, np.nan, 140],
    'Temp': [27, 12, 38, np.nan, 32],
    'Humidity': [1200, 1890, 2300, np.nan, 2100]
}
frame = DataFrame(data)
print(frame)
print('\n')

# Filtering
frame = frame.dropna()
print('\n')

# Instaed of dropping, you can fill it with some data
print(frame.fillna(0))