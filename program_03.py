# 3. Add some data to an existing Series
import pandas as pd

s = pd.Series([10, 20, 30])
print("Original Series:")
print(s)

new_data = pd.Series([40, 50])
s = pd.concat([s, new_data], ignore_index=True)

print("Series after adding data:")
print(s)
