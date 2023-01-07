# student_scores = input("Input a list of student scores.")
# for n in range(0, len(student_scores)):
#     student_scores[n] = int(student_scores[n])
# print(student_scores)

# student_scores = input("Input a list of student scores.")
# for n in range(0, len(student_scores)):
#     student_scores[n] = int(student_scores[n])
# print(student_scores)

# student_scores = [123, 232, 323, 232, 121]
# highest_score = 0
# for score in student_scores:
#     if score > highest_score:
#         highest_score = score
# print(f"The highest score is: {highest_score}")
#
sum_of_even = 0
for number in range(2, 101, 2):
    sum_of_even += number
print(sum_of_even)

sum_of_even1 = 0
for number in range(0, 101):
    if number % 2 == 0:
        sum_of_even1 += number
print(sum_of_even1)
