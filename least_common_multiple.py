# Find the least common multiple of 2 numbers

def least_common_multiple(number1, number2):
	# algorithm
	# initialize num as the max of number1 and number2
	# while num is not common muliple
	#    increase num
	# return num
	# num = max(number1, number2)
	# while num % number1 != 0 or num % number2 != 0:
	# 	num += 1
	# return num
	num = max(number1, number2)
	while True:
		if num % number1 == 0 and num % number2 == 0:
			return num
		num += 1

result = least_common_multiple(15, 10)
print(result)
# import random
# num1 = random.randint(1, 1000)
# num2 = random.randint(1, 1000)
# result = least_common_multiple(num1, num2)
# print(f"num1: {num1}, num2: {num2}, lcm: {result}")
# print(greatest_common_divisor(225, 1710))