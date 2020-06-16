# solve quadration equation
# a x ^2 + b x + c = 0

import math
def quad_equation_solver(a, b, c):
# formula is
#    x = (-b + sqrt(b^2-4 a c ))/ 2a , (-b - sqrt(b^2-4 a c ))/2a
	term = b * b - 4 * a * c
	if term > 0:
		sq = math.sqrt(term)
		ans1 = (-b+sq) /(2.0 * a)
		ans2 = (-b-sq)/(2.0*a)
		return [ans2, ans1]
	elif term == 0:
		return [-b / (2.0 * a)]
	else:
		return []


print(quad_equation_solver(1, -3, 2))
