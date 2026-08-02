# 2. Arithmetic operations on two Pandas Series
import pandas as pd

s1 = pd.Series([10, 20, 30, 40])
s2 = pd.Series([1, 2, 3, 4])

print("Addition:")
print(s1 + s2)

print("Subtraction:")
print(s1 - s2)

print("Multiplication:")
print(s1 * s2)

print("Division:")
print(s1 / s2)
