# symmetric triangle
def print_symmetric_triangle(width, height):
	for y in range(height):
		x = int(y * (width-1) / (height-1))+1
		offset = " " * (width-x)
		print(offset + "*" * (2*x-1))

print_symmetric_triangle(10, 7)		