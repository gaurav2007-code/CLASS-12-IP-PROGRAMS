# 12. Import/Export CSV and show basic info about the DataFrame
import pandas as pd

data = {
    'Adm_No': [101, 102, 103],
    'Gender': ['M', 'F', 'M'],
    'Percentage': [80, 90, 70]
}
df = pd.DataFrame(data)

df.to_csv('Student_result.csv', index=False)

df = pd.read_csv('Student_result.csv')

print("Row Labels:", df.index)
print("Column Labels:", df.columns)
print("Data Types:")
print(df.dtypes)
print("Dimensions:", df.ndim)
print("Shape:", df.shape)
