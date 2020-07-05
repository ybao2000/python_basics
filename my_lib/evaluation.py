def split_simple_expr_1(expr):
	'''
		split_simple_expr_1(string) => []
		
		split a simple expression (no brackets) into list
		iterate through the expr
		expr: string
	'''
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

def split_simple_expr_2(expr):
	'''
		split_simple_expr_2(string) => []	

		split a simple expression (no brackets) into list
		using the trick of replace
		expr: string
	'''	
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
 
def calc_simple_expr(list_expr):
	'''
	calc_simple_expr([]) => float

	given a list from expression, calculate the result
	list_expr: []
	'''
	# first round, handle * and /
	stack = []
	while len(list_expr) > 0:
		item = list_expr.pop(0)
		if item == '*':
			num1 = float(stack.pop())
			num2 = float(list_expr.pop(0))
			num = num1 * num2
			stack.append(num)
		elif item == '/':
			num1 = float(stack.pop())
			num2 = float(list_expr.pop(0))
			num = num1 / num2
			stack.append(num)
		else:
			stack.append(item)
	# second round handle '+', '-'
	num = float(stack.pop(0))
	while len(stack) > 0:
		oper = stack.pop(0)
		if oper == '+':
			if(len(stack) == 0):
				return 'invalid'			
			num_next = float(stack.pop(0))
			num += num_next
		elif oper == '-':
			if(len(stack) == 0):
				return 'invalid'
			num_next = float(stack.pop(0))
			num -= num_next			
		else:
			return 'invalid'
	return num

def my_eval(expr):
	'''
		eval(str) => float 

		evaluate the string and return the result
	'''
	# list_expr = split_simple_expr_1(expr)
	# return calc_simple_expr(list_expr)
	return calc_simple_expr(split_simple_expr_1(expr))
