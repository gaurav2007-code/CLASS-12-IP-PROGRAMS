# 21. Replace all missing values in a DataFrame with 999
import pandas as pd
import numpy as np

df = pd.DataFrame({'A': [1, np.nan, 3], 'B': [np.nan, 5, 6]})

print("Original Data:")
print(df)

df = df.fillna(999)

print("After Filling Missing Values:")
print(df)
