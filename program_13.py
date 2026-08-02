# 13. Display selected columns and first/last 5 records
import pandas as pd

df = pd.read_csv('Student_result.csv')

print("Selected Columns:")
print(df[['Adm_No', 'Gender', 'Percentage']])

print("First 5 Records:")
print(df.head())

print("Last 5 Records:")
print(df.tail())
