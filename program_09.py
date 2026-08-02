# 9. Append a list of dictionaries to an existing DataFrame
import pandas as pd

df = pd.DataFrame({'A': [1, 2], 'B': [3, 4]})
print("Original DataFrame:")
print(df)

new_rows = [{'A': 3, 'B': 4}, {'A': 5, 'B': 6}]
new_df = pd.DataFrame(new_rows)

df = pd.concat([df, new_df], ignore_index=True)
print("After Appending:")
print(df)
