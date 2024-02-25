# student/college_details.py

class CollegeDetails:
    def __init__(self, college_name, location):
        self.college_name = college_name
        self.location = location

    def display_college_details(self):
        print("College Name:", self.college_name)
        print("Location:", self.location)
