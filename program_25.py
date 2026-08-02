# 25. Analyse student performance parameters
import pandas as pd

data = {
    'Name': ['A', 'B', 'C', 'D'],
    'Marks': [78, 85, 62, 90]
}
df = pd.DataFrame(data)

print(df)

print("Average Marks:", df['Marks'].mean())
print("Highest Marks:", df['Marks'].max())
print("Lowest Marks:", df['Marks'].min())
