# in my case, n is always > 1
import math
tolerance = 1.e-8
count = 0

def my_sqrt(n):
	return sqrt_recursive(1, n, n)

# recursive

def sqrt_recursive(start, end, target):
	global count
	mid = (start + end) / 2.0
	result = mid * mid
	# stop: if the result is close enough
	if abs(result-target) < tolerance:
		return mid
	# if result is smaller, then use the right half range
	elif result < target:
		count += 1
		return sqrt_recursive(mid, end, target)
	# otherwise (result is larger), then use the left half range
	else:
		count += 1
		return sqrt_recursive(start, mid, target)


# print(my_sqrt(3))
# print(math.sqrt(3))
# print(count)