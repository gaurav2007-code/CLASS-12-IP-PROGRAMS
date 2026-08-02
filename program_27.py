# 27. Bar chart of highest scores per subject
import matplotlib.pyplot as plt

subjects = ['Eng', 'Math', 'Sci', 'SSt', 'Comp']
highest_scores = [95, 99, 96, 92, 100]

plt.bar(subjects, highest_scores, color='green')
plt.xlabel('Subject')
plt.ylabel('Highest Score')
plt.title('Highest Scores per Subject')

max_score = max(highest_scores)
max_subject = subjects[highest_scores.index(max_score)]
print("Highest Score:", max_score, "in", max_subject)

plt.show()
