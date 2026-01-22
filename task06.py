class Student:
    def __init__(self, name: str, age: int, grade: str):
        self.name = name
        self.age = age
        self.grade = grade

    def info(self) -> None:
        print(f"{self.name}, {self.age} yoshda, {self.grade} o‘quvchisi.")


student1 = Student("Ali", 15, "9-sinf")
student2 = Student("Dilnoza", 16, "10-sinf")

student1.info()
student2.info()
