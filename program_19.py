# 19. Subtract the mean of a row from each element of the row
import pandas as pd

df = pd.DataFrame({'A': [10, 20], 'B': [30, 40]})

row_mean = df.mean(axis=1)
result = df.sub(row_mean, axis=0)

print(result)
