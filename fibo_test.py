fibo = {0:0, 1:1}
def fibo_recursive(n):
	if n==0:
		return 0
	elif n==1:
		return 1
	else:
		if n-1 in fibo:
			term_1 = fibo[n-1]
		else:
			term_1 = fibo_recursive(n-1)
		if n-2 in fibo:
			term_2 = fibo[n-2]
		else:
			term_2 = fibo_recursive(n-2)
		term = term_1+term_2
		fibo[n] = term
		return term
		
# print(fibo_recursive(100))

# 0, 1, 1, 2, 3, 5, 8, 13, 21, 34, 55, ...
# a[n] = a[n-1] + a[n-2]
def fibo_loop_list(n):
	if n == 0:
		return 0
	elif n == 1:
		return 1
	else:
		fibo = [0, 1]
		for i in range(2, n+1):
			fibo.append(fibo[i-1] + fibo[i-2])
	return fibo[n]

def fibo_loop_dict(n):
	if n == 0:
		return 0
	elif n == 1:
		return 1
	else:
		fibo = {0: 0, 1: 1}
		for i in range(2, n+1):
			fibo[i] = fibo[i-1] + fibo[i-2]
	return fibo[n]

# print(fibo_loop_dict(100000))

print(fibo_recursive(1000))