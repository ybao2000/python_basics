# input is a list ['1', '+', '2', '*', '4', '-', '5', '/', '6']
# steps
# create an empty stack 
# read the list one by one
#    if item is * or /, read the next item from list, pop the item from stack , 
# 						do the calculation, and push back 
#    otherwise, push back
#   ----------------------------
#    '1', '+', '8', '-', '0.8'
#    pop the item from the stack one by one
#    if item is '+' or '-', pop the next item , and do the calculation, don't push it back
#    
def calc_simple_expr(list_expr):
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

# expr = ['1', '+', '2', '*', '3', '-', '4', '/', '5']
expr = ['3', '+', '15', '*', '7', '*', '8', '-', '6', '/', '3', '+', '2', '-', '1']
print(expr)
print(calc_simple_expr(expr))

