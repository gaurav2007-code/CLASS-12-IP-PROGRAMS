# 10. Filter rows using relational and logical operators
import pandas as pd

df = pd.DataFrame({
    'Age': [17, 19, 21],
    'Score': [85, 75, 90]
})

print("Students with Age > 18 and Score >= 80:")
print(df[(df['Age'] > 18) & (df['Score'] >= 80)])
