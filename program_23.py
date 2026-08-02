# 23. Group by category and print total expenditure
import pandas as pd

data = {
    'category': ['Office', 'Office', 'Tech', 'Tech'],
    'item_name': ['Pens', 'Paper', 'Mouse', 'Laptop'],
    'expenditure': [500, 300, 1200, 45000]
}
df = pd.DataFrame(data)

grouped = df.groupby('category')['expenditure'].sum()

print("Total Expenditure by Category:")
print(grouped)
