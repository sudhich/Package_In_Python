#main.py

import sys
import os
# Get the current directory
current_dir = os.path.dirname(__file__)
# Add the parent directory to the Python module search path
parent_dir = os.path.abspath(os.path.join(current_dir, os.pardir))
sys.path.append(parent_dir)

# Importing the entire package
import math_operations

# Importing specific modules from the package
from math_operations import addition, subtraction


# Using functions from the package
result_add = addition.add(5, 3)
result_sub = subtraction.subtract(10, 4)

print("Result of addition:", result_add)
print("Result of subtraction:", result_sub)
