# 8. Join two dataframes along columns
import pandas as pd

df1 = pd.DataFrame({'A': [1, 2]})
df2 = pd.DataFrame({'B': [3, 4]})

result = pd.concat([df1, df2], axis=1)
print("Combined along columns:")
print(result)
