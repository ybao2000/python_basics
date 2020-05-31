# randomly given a number between 1 and 10, 
# how many times to reproduce the same number

import random

def number_to_reproduce():
	s = set()
	icount = 0
	while True:
		num = random.randint(1, 10)
		icount += 1
		if num in s:
			return icount
		else:
			s.add(num)


TEST_NUMBER = 100000
sum = 0
for i in range(TEST_NUMBER):
	iCount = number_to_reproduce()
	sum += iCount

average = sum/TEST_NUMBER

print(average)
