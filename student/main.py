# main.py


import sys
import os
# Get the current directory
current_dir = os.path.dirname(__file__)
# Add the parent directory to the Python module search path
parent_dir = os.path.abspath(os.path.join(current_dir, os.pardir))
sys.path.append(parent_dir)



from student import details, marks, college_details

# Creating objects of classes from different modules
student_info = details.StudentDetails("RamShyam", "12345")
student_info.display_details()

math_marks = marks.StudentMarks("Python", 90)
math_marks.display_marks()

college_info = college_details.CollegeDetails("St. Mary's College", "Deshmukhi")
college_info.display_college_details()
