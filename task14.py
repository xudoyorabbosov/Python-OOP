class Student:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def show_info(self):
        print(f"{self.name} — {self.age} yosh")

students = [
    Student("Ali", 15),
    Student("Laylo", 16),
    Student("John", 17),
    Student("Malika", 14),
    Student("Olim", 18)
]

oldest = max(students, key=lambda s: s.age)
oldest.show_info()
