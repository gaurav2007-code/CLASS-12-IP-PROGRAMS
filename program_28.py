# 28. Line chart showing average score of each subject
import matplotlib.pyplot as plt

subjects = ['Eng', 'Math', 'Sci', 'SSt', 'Comp']
avg_scores = [78, 82, 80, 75, 88]

plt.plot(subjects, avg_scores, marker='o', color='red')
plt.xlabel('Subject')
plt.ylabel('Average Score')
plt.title('Average Scores per Subject')
plt.show()
