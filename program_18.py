# 18. Locate the 3 largest values in a DataFrame column
import pandas as pd

df = pd.DataFrame({'A': [10, 50, 20, 40, 30]})

print("3 Largest Values:")
print(df['A'].nlargest(3))
