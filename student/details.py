# student/details.py

class StudentDetails:
    def __init__(self, name, roll_number):
        self.name = name
        self.roll_number = roll_number

    def display_details(self):
        print("Name:", self.name)
        print("Roll Number:", self.roll_number)
