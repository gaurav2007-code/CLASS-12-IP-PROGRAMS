# 26. Bar chart showing school results for 5 consecutive years
import matplotlib.pyplot as plt

years = ['2020', '2021', '2022', '2023', '2024']
pass_percentage = [92, 95, 93, 97, 99]

plt.bar(years, pass_percentage, color='skyblue')
plt.xlabel('Year')
plt.ylabel('Pass Percentage')
plt.title('School Results Over 5 Years')
plt.show()
