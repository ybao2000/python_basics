# Give width and height, pring a solid left triangle with *
def print_left_triangle(width, height):
	for y in range(height):
		x = int(y * (width-1) / (height-1))+1
		offset = " " * (width-x)
		print(offset + "*" * x)

print_left_triangle(20, 10)	