# 5. Select rows where percentage is between 70 and 90
import pandas as pd

df = pd.DataFrame({
    'Name': ['A', 'B', 'C', 'D'],
    'Percentage': [65, 75, 85, 95]
})

print("Students with Percentage between 70 and 90:")
print(df[(df['Percentage'] >= 70) & (df['Percentage'] <= 90)])
