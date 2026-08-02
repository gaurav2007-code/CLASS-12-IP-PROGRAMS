# 11. Filter out duplicate rows
import pandas as pd

df = pd.DataFrame({'A': [1, 2, 2, 3]})
print("Original Data:")
print(df)

print("Without Duplicates:")
print(df.drop_duplicates())
