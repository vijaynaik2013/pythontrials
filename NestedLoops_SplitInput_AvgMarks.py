n = int(input("please enter the number of students:"))
a = {}
for i in range(n):
    name, *line = input().split()
    scores = list(map(float, line))
    a[name] = scores
print(a)
student_name_for_avg_Score = a [input("please enter name of student for average score:")]
avg = sum(student_name_for_avg_Score)/len(student_name_for_avg_Score)
print('%.2f'%avg)






