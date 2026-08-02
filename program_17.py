# 17. Find the sum of each column and the column with the lowest mean
import pandas as pd

df = pd.DataFrame({'A': [10, 20], 'B': [30, 40]})

print("Sum of each column:")
print(df.sum())

print("Column with lowest mean:", df.mean().idxmin())
