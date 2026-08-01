import numpy as np

marks = np.array([
    [85, 78, 92],  # Student 1
    [36, 45, 50],  # Student 2
    [90, 82, 94],  # Student 3
    [65, 70, 72],  # Student 4
    [88, 90, 85]   # Student 5
], dtype=float)

print("--- RAW MARKS MATRIX ---")
print(marks)


mean_subjects = np.mean(marks, axis=0)
max_subjects = np.max(marks, axis=0)
min_subjects = np.min(marks, axis=0)


print("\n--- SUBJECT METRICS (Math, Science, English) ---")
print(f"Class Average:     {mean_subjects}")
print(f"Highest Score:     {max_subjects}")
print(f"Lowest Score:      {min_subjects}")


# Individual Student Metrics 

total_per_student = np.sum(marks, axis=1)
total_avg_student = np.mean(marks, axis=1)

print("\n--- INDIVIDUAL STUDENT METRICS ---")
for i, (total, avg) in enumerate(zip(total_per_student, total_avg_student)) :
    print(f"Student {i+1} -> total marks : {total:.1f} avg marks : {avg:.2f}")


# Grading Criteria & Boolean Mask Filtering
passing_score = 40

# Check if student passed ALL three subjects
passed_all = np.all(marks > passing_score, axis=1)
print("\n--- PASS/FAIL STATUS (All Subjects >= 40) ---")
for i, status in enumerate(passed_all):
  result = "PASSED" if status else "FAILED"
  print(f"Student {i+1} -> {result}")