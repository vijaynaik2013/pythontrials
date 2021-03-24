n = int(input("please enter the number of students:"))
a = {}
for _ in range(n):
    name = input("please enter the name of student:")
    marks = []
    for _ in range(3):
        x = float(input("please enter marks:"))
        marks.append(x)
    a[name]=marks
print(a)
student_name_for_avg_Score = a [input("please enter name of student for average score:")]
avg = sum(student_name_for_avg_Score)/len(student_name_for_avg_Score)
print(round(avg, 2))






