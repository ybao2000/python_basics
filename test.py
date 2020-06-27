import my_sqrt
from grade_a_mark import grade_a_mark
import random

print(my_sqrt.my_sqrt(3))
mark = random.randint(0, 100)
print(f"mark is {mark}, grade is {grade_a_mark(mark)}")