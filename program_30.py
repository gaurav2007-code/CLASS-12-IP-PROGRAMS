# 30. Data aggregation, summary and visualization
import pandas as pd
import matplotlib.pyplot as plt

data = {
    'Region': ['North', 'South', 'East', 'West'],
    'Users': [1500, 2200, 1800, 2900]
}
df = pd.DataFrame(data)

print(df)
print("Total Users:", df['Users'].sum())

plt.pie(df['Users'], labels=df['Region'], autopct='%1.1f%%')
plt.title('User Distribution by Region')
plt.show()
