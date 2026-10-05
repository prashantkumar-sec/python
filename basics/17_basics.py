# Practice Task: Student Manager
# Create a Student class with the following:
#
# Attributes
    # name
    # roll_no
    # marks, an empty list that starts blank for every student
# Methods
    # add_marks(m): adds one mark to the marks list.
    # average(): returns the average of the marks. If the list is empty, it must not crash (use an if check or try/except, e.g. return 0).
    # __str__(): returns a string like "Prashant (Roll 12): avg 78.5".
# Main program
    # Create 3 students.
    # Add at least 3 marks to each one.
    # Put all the students in a list and loop through it, printing each student.

class Student:
    def __init__(self, name, roll_no):
        self.name = name
        self.roll_no = roll_no
        self.marks = []

    def average(self):
        if len(self.marks) == 0:
            return 0
        return sum(self.marks)/len(self.marks)

    def add_marks(self,m):
        self.marks.append(m)

    def __str__(self):
        return f"{self.name} (Roll {self.roll_no}): avg {self.average()} "

s1 = Student("Prashant Kumar", "024101010110")
s1.add_marks(80)
s1.add_marks(60)
s1.add_marks(76)
s1.add_marks(90)
s2 = Student("Prince", "024101010113")
s2.add_marks(83)
s2.add_marks(63)
s2.add_marks(79)
s2.add_marks(93)
s3 = Student("Shikha Kumari", "025101010130")
s3.add_marks(83)
s3.add_marks(67)
s3.add_marks(89)
s3.add_marks(95)

students = [s1,s2,s3]

for student in students:
    print(student)

top = max(students, key=lambda s: s.average())
print(f"Topper {top.name}")