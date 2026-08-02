import numpy as np
import pandas as pd

# 1. Creating a Pandas Series from a dictionary of values
info_dict = {"Apple": 150, "Banana": 60, "Cherry": 200, "Mango": 120}
series_from_dict = pd.Series(info_dict)

print("--- Series Created From Dictionary ---")
print(series_from_dict)
print()

# 2. Creating a Pandas Series from an ndarray (NumPy array)
array_data = np.array([10, 20, 30, 40, 50])
# Optional: providing custom index labels
series_from_array = pd.Series(array_data, index=["A", "B", "C", "D", "E"])

print("--- Series Created From ndarray ---")
print(series_from_array)
