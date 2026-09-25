class student:
    def student(self, name):
        self.name = name
        return self.name
class student1(student):
    def __init__(self, name, age):
        super().student(name)
        self.age = age
    def display(self):
        print("Student Name:", self.name)
        print("Age:", self.age)