# class MySpecialException(Exception):
#   pass

a = int(input("enter a non-negative value: "))

if a < 0:
  raise Exception("x cannot be less than 0")

import math
print(math.sqrt(a))
