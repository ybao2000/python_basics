# print january

#          1  2  3  4
# 5  6  7  8  9  10 11
# 12 13 14 15 16 17 18
# 19 20 21 22 23 24 25
# 26 27 28 29 30 31

# def print_jan(title, indent, max_num):
# for jan, title = 'Jan', indent= 3, max_num = 31

def print_month(title, indent, max_num):
	print(title)
	print('   '*indent, end='')
	for num in range(1, max_num+1):
		print(f"{num:2d} ", end='')
		if (num+indent) % 7 == 0:
			print()

# title = 'Jan'
# indent = 3
# max_num = 31
# print_month(title, indent, max_num)


# title = 'Feb'
# indent = 6
# max_num = 29
# print_month(title, indent, max_num)

def make_lines(indent, max_num):
	lines = []
	line = '   '*indent
	for num in range(1, max_num+1):
		line += f"{num:2d} "
		if (num+indent) % 7 == 0:
			lines.append(line)
			line = ''
	if line:
		# make a full line (21)
		line += ' ' * (21-len(line))   # this is to make length of line to be 21 (if short, add empty space ' ')
		lines.append(line)
	return lines

# lines = make_lines(3, 31)
# for line in lines:
# 	print(line)
months = {'Jan': 31, 'Feb': 29, 'Mar': 31, 'Apr': 30, 'May': 31, 'Jun': 30, 'Jul': 31, 'Aug': 31, 'Sep': 30, 'Oct': 31, 'Nov': 30, 'Dec': 31}
# first_indent = 3

def get_line(list_line, i):
	if i<len(list_line):
		return list_line[i]
	else:
		return ' ' * 21

# print 3 month
def print_three_month(first_indent, title1, title2, title3):
	print(title1, title2, title3, sep=' '*20)
	max_num_1 = months[title1]
	max_num_2 = months[title2]
	max_num_3 = months[title3]
	indent1 = first_indent
	indent2 = (indent1 + max_num_1) % 7
	indent3 = (indent2 + max_num_2) % 7
	list_1 = make_lines(indent1, max_num_1)
	list_2 = make_lines(indent2, max_num_2)
	list_3 = make_lines(indent3, max_num_3)

	max_len = max(len(list_1), len(list_2), len(list_3))

	for i in range(max_len):
		line1 = get_line(list_1, i)
		line2 = get_line(list_2, i)
		line3 = get_line(list_3, i)
		print(line1, line2, line3, sep='  ')
	
	return (first_indent + max_num_1 + max_num_2 + max_num_3) % 7

first_indent = 3
next_indent = print_three_month(first_indent, 'Jan', 'Feb', 'Mar')
next_indent = print_three_month(next_indent, 'Apr', 'May', 'Jun')
next_indent = print_three_month(next_indent, 'Jul', 'Aug', 'Sep')
print_three_month(next_indent, 'Oct', 'Nov', 'Dec')