stack = []
stack.append('1')
stack.append('+')
stack.append('2')
stack.append('*')
stack.append('4')
stack.append('-')
stack.append('5')
stack.append('/')
stack.append('6')

print(stack, type(stack))
while len(stack) > 0:
	item = stack.pop()
	print(item)