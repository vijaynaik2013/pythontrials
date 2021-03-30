class Student:
    def __init__(self,name,marks):
        self.name = name
        self.marks= marks

    def average(self):
        return sum(self.marks)/len(self.marks)

student1 = Student(name='vijay',marks=(1,2,3))
student2 = Student(name='Babuii',marks=(4,5,6))

print(student1.average())
print(student2.average())


