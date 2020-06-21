### example of stack

def f1(num):
	res1 = f2(num)+1
	return res1

def f2(num):
	res2 =  f3(num)+2
	return res2

def f3(num):
	res3 =  f4(num)+3
	return res3

def f4(num):
	res4 = num + 4
	return res4


print(f1(100))