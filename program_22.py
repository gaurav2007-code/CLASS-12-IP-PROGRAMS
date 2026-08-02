# 22. Print all elements of a Series above the 75th percentile
import pandas as pd

s = pd.Series([10, 20, 30, 40, 50, 60, 70, 80, 90, 100])

value_75 = s.quantile(0.75)
print("75th Percentile Value:", value_75)

print("Elements above 75th percentile:")
print(s[s > value_75])
