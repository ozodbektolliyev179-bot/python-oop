class Student:
    def __init__(self, name: str, age: int, grade: str):
        self.name = name
        self.age = age
        self.grade = grade


student1 = Student("Aliyev Vali", 15, "9-sinf")
student2 = Student("Karimova Dilnoza", 16, "10-sinf")
student3 = Student("Rahmonov Aziz", 14, "8-sinf")


print(student1.name, student1.age, student1.grade)
print(student2.name, student2.age, student2.grade)
print(student3.name, student3.age, student3.grade)
