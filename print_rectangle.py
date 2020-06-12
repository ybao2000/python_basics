# Given width and height, print a solid rectangle with *
def print_rectangle(width, height):
#  3, 4
#  ***
#  ***
#  ***
#  ***
# string can be multipled
# print('*'*100)
	for h in range(height):
		print('*'*width)

print_rectangle(50, 5)
