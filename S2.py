questions = int(input())
student = []
teacher = []
correct = 0
for i in range(questions):
    hold = input()
    student.append(hold)

for x in range(questions):
    hold = input()
    teacher.append(hold)

for p in range(questions):
    if student[p] == teacher[p]:
        correct = correct +1

print(correct)