def binary(num):
	val = num
	arr = []
	while val > 0:
		arr.insert(0, str(val%2))
		val = val//2
	return ''.join(arr)

def isPalindrome(s):
	size = len(s)
	left = 0
	right = size-1
	while left < right:
		if s[left] != s[right]:
			return False
		left += 1
		right -=1
	return True

sum = 0
for num in range(1, 1000000):
	strNum = str(num)
	strBin = binary(num)
	if isPalindrome(strNum) and isPalindrome(strBin):
		sum += num

print(sum)
