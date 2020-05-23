# Find the greatest common divisor of 2 numbers

def greatest_common_divisor(number1, number2):
	# algorithm from small to bigger
	# initialize the result to 1
	# for loop from 1 to number1
	# 	check num to see if num is common divisor, if yes, update result
	# after the loop, result is the answer
	# result = 1
	# for num in range(2, number1+1):
	# 	if number1 % num == 0 and number2 % num == 0:
	# 		result = num

	# return result

	# algorithm from big to smaller
	# num = min(number1, number2)
	# while num >= 1:
	# 	if number1 % num == 0 and number2 % num == 0:
	# 		return num
	# 	num -= 1
	# return num

	highest = min(number1, number2)
	for num in range(highest, 0, -1):
		if number1 % num == 0 and number2 % num == 0:
			return num

import random
import math
num1 = random.randint(1, 1000)
num2 = random.randint(1, 1000)
result = greatest_common_divisor(num1, num2)
math_result = math.gcd(num1, num2)
print(f"num1: {num1}, num2: {num2}, gcd: {result}, math gcd: {math_result}")
# print(greatest_common_divisor(225, 1710))

