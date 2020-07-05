# global a
a = 1

def foo_1():
	global a
	a = 2
	def foo_2():
		global a		
		a = 3
		print("foo_2", a)

	foo_2()
	print("foo_1", a)


# print a from the function
foo_1()
print("global", a)
# print a outside the function
# global a
print(a)