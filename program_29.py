# 29. Charts for gender count and average percentage
import matplotlib.pyplot as plt

genders = ['Female', 'Male']
counts = [45, 55]
avg_percentage = [78.5, 74.2]

plt.subplot(1, 2, 1)
plt.bar(genders, counts, color=['pink', 'blue'])
plt.title('Number of Students')

plt.subplot(1, 2, 2)
plt.bar(genders, avg_percentage, color=['purple', 'teal'])
plt.title('Average Percentage')

plt.show()
