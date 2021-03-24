n = int(input())
a = {}
for _ in range(n):
    name = input()
    marks = []
    for _ in range(3):
        x = float(input())
        marks.append(x)
    a[name]=marks
student_name_for_avg_Score = a [input()]
avg = sum(student_name_for_avg_Score)/len(student_name_for_avg_Score)
print(round(avg,2))
