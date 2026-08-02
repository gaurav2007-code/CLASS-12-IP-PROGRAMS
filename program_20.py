# 20. Replace all negative values in a DataFrame with 0
import pandas as pd

df = pd.DataFrame({'A': [-1, 2, -3], 'B': [4, -5, 6]})

print("Original Data:")
print(df)

df[df < 0] = 0

print("After Replacing Negative Values:")
print(df)
