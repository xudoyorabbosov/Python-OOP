class Student:
    def __init__(self, name, age, grade):
        self.name = name
        self.age = age
        self.grade = grade

s1 = Student("Ali", 15, 9)
s2 = Student("Barno", 14, 8)
print(s1.name, s2.grade)
