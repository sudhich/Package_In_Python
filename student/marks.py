# student/marks.py

class StudentMarks:
    def __init__(self, subject, marks):
        self.subject = subject
        self.marks = marks

    def display_marks(self):
        print("Subject:", self.subject)
        print("Marks:", self.marks)
