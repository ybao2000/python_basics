# symmetric triangle
def print_christmas_tree(size, height):
	for y in range(size):
		x = y+1
		offset = " " * (size-x)
		print(offset + "*" * (2*x-1))
	for leg in range(height):
		print(' ' * (size-2) + '***')
print_christmas_tree(20, 15)		