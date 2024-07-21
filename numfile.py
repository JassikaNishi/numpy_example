import numpy as np
import matplotlib.pyplot as plt

data = np.genfromtxt('data.csv', delimiter=',', skip_header=1)
roll = data[:, 0]
marks = data[:, 1:]

total_marks = np.sum(marks, axis=1)
max_marks = 300
percentages = (total_marks / max_marks) * 100

class_averages = np.mean(marks, axis=0)
toppers = np.argmax(marks, axis=0)

print("Class Averages:")
for i in range(len(class_averages)):
    avg = class_averages[i]
    print("Subject", i+1, ":", avg)

print("\nToppers:")
for i in range(len(toppers)):
    topper = toppers[i]
    print("Subject", i+1, ":", "Roll", roll[topper], "with", marks[topper, i], "marks")

plt.figure(figsize=(10, 6))
plt.hist(percentages, bins=10, edgecolor='black')
plt.title("Histogram of Student Percentages")
plt.xlabel("Percentage")
plt.ylabel("Frequency")
plt.show()

print("\nStudent-wise Percentages:")
for i in range(len(roll)):
    r = roll[i]
    p = percentages[i]
    print("Roll", r, ":", p, "%")

print("\nAdditional Statistics:")
print("Overall Highest Score:", np.max(marks))
print("Overall Lowest Score:", np.min(marks))
print("Standard Deviation of Percentages:", np.std(percentages))


rankings = np.argsort(total_marks)[::-1]
print("\nTop 5 Students:")
for i in range(5):
    rank = rankings[i]
    print("Rank", i+1, ":", "Roll", roll[rank], "with", percentages[rank], "%")

for i in range(marks.shape[1]):
    subject_marks = marks[:, i]
    print("\nSubject", i+1, "Analysis:")
    print("Mean:", np.mean(subject_marks))
    print("Median:", np.median(subject_marks))
    print("Standard Deviation:", np.std(subject_marks))
    print("25th Percentile:", np.percentile(subject_marks, 25))
    print("75th Percentile:", np.percentile(subject_marks, 75))
