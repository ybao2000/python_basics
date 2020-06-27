# give a string of arithematic expression
# return a list
# '-331+14 -7*9' => ['-331', '+', '14', '-', '7', '*', '9']

def split_simple_expr_1(expr):
	result =[]   # <--- this is going to be the final result
	term = []    # <--- this the working list, 
	for char in expr:  # <--- loop throught the expression
		if char == '-' and not term:
			term.append(char)
		elif char == '+' or char == '-' or char == '*' or char == '/':   # <--- if +, -, *, /, then split
			if term:
				result.append(''.join(term))	# if something is in term, then put term in result
				term = []
			result.append(char)
		elif char != ' ':  # append char into term only if it's not space
			term.append(char)
	if term:
		result.append(''.join(term))	# if something is in term, then put term in result		
	return result

# expr = '-331+14 -7*9'
# print(split_simple_expr_1(expr))

def split_simple_expr_2(expr):
	if expr.startswith('-'):
		expr2 = expr[1:]
		expr2 = expr2.replace(' ', '').replace('+', ' + ').replace('-', ' - ').replace('*', ' * ').replace('/', ' / ')
		list_expr = expr2.split(' ')
		list_expr[0] = '-'+list_expr[0]
		return list_expr
	else:
		# expr2 = expr.replace(' ', '').replace('+', ' + ').replace('-', ' - ').replace('*', ' * ').replace('/', ' / ')
		# return expr2.split(' ')
		return expr.replace(' ', '').replace('+', ' + ').replace('-', ' - ').replace('*', ' * ').replace('/', ' / ').split(' ')
expr = '-331+14 -7*9'
print(split_simple_expr_2(expr))
