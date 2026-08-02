# 24. Generate descriptive statistics from sales data
import pandas as pd

data = {'Sales': [100, 250, 300, 400, 500]}
df = pd.DataFrame(data)

print("Mean:", df['Sales'].mean())
print("Median:", df['Sales'].median())
print("Mode:", df['Sales'].mode()[0])
print("Variance:", df['Sales'].var())
print("Standard Deviation:", df['Sales'].std())
