# 6. Change the percentage in a given row entered by the user
import pandas as pd

df = pd.DataFrame({
    'Percentage': [70, 80, 90]
}, index=['R1', 'R2', 'R3'])

print("Before Update:")
print(df)

row = input("Enter row label to update (R1/R2/R3): ")
new_value = float(input("Enter new percentage: "))

df.loc[row, 'Percentage'] = new_value

print("After Update:")
print(df)
