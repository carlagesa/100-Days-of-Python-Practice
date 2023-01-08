student_scores = {
    "Harry": 72,
    "Carlton": 98,
    "Laureen": 10,
    "Drogo": 74,
}
for key in student_scores:
    # print(student_scores[key])
    if student_scores[key] >= 91 and student_scores[key] <= 100:
        student_scores[key] = "Outstanding"
    elif student_scores[key] >= 81 and student_scores[key] <= 90:
        student_scores[key] = "Exceeds expectations"
    elif student_scores[key] >= 71 and student_scores[key] <= 80:
        student_scores[key] = "Acceptable"
    else:
        student_scores[key] = "Fail"
student_grades = student_scores

print(student_grades)
