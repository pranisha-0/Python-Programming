class Student:
    def __init__(self, name, roll, marks):
        self.n= name
        self.r = roll
        self.m = marks
    def display(self):
        print(f"Name: {self.n}")
        print(f"Roll No: {self.r}")
        print(f"Marks: {self.m}")

s = Student("Pranisha", 21, 99)
s.display()