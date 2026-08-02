# 7. Join two dataframes along rows
import pandas as pd

df1 = pd.DataFrame({'A': [1, 2]})
df2 = pd.DataFrame({'A': [3, 4]})

result = pd.concat([df1, df2], axis=0, ignore_index=True)
print("Combined along rows:")
print(result)
