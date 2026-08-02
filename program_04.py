# 4. Select the rows where percentage is greater than 70
import pandas as pd

df = pd.DataFrame({
    'Name': ['Ali', 'Ben', 'Cid'],
    'Percentage': [65, 85, 72]
})

print("Full Data:")
print(df)

print("Students with Percentage > 70:")
print(df[df['Percentage'] > 70])
