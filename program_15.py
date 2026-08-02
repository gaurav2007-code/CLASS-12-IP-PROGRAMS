# 15. Create a duplicate file with selected columns and find highest percentage
import pandas as pd

df = pd.read_csv('Student_result.csv')

df['Name'] = ['Amit', 'Bhavna', 'Chirag']   # sample names added

dup_df = df[['Adm_No', 'Name', 'Percentage']]
dup_df.to_csv('student_result_duplicate.csv', index=False)

max_row = df[df['Percentage'] == df['Percentage'].max()]
print("Student with Highest Percentage:")
print(max_row)
