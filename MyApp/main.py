# main.py

import sys
import os
# Get the current directory
current_dir = os.path.dirname(__file__)
# Add the parent directory to the Python module search path
parent_dir = os.path.abspath(os.path.join(current_dir, os.pardir))
sys.path.append(parent_dir)



from MyApp import functions, greet

power=functions.power(3,2)
print(power)
# Now you can use functions from the functions module

greet.SayHellow("Fanit")
avg=functions.average(4,8)
print(avg)

print(functions.sum(12,34))