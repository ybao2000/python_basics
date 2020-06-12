# Give width and height, pring a solid right triangle with *
def print_right_triangle(width, height):
	for y in range(height):
		x = int(y * (width-1) / (height-1))+1
		print('*'*x)

print_right_triangle(20, 10)