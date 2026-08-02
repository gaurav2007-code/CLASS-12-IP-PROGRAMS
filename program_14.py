# 14. Rename columns and replace percentage below 40 with NaN
import pandas as pd
import numpy as np

df = pd.read_csv('Student_result.csv')

df.columns = ['Admission_Number', 'Sex', 'Final_Percentage']

df.loc[df['Final_Percentage'] < 40, 'Final_Percentage'] = np.nan

print(df)
