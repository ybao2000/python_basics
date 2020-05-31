#### how many peaches were there at least in the beginning

#### solve it ####
# just try each number, start from 1
# first step, total1 => 5 pile1 + 1 (this has to be satisfied, otherwiser, the number is not valid, increase the number and try the increased number)
#    second step, total2 = 4 * pile1 => 5 pile2 + 1 (this has to be satisfied, otherwise, the number is wrong, increase the number and try the increased number), 
#     	third step, total3 = 4 * pile2 => 5 pile3 + 1 (this has to be satisfied, otherwise, the number is wrong, increase the number, and try the increased number) 	
#					fourth step, total4 = 4 * pile3 => 5 pile4 + 1 (this has to satified, otherwise, the number is wrong, increase the number and try the increased number)
#						fifth step, total5 = 4 * pile4 => 5 pile5 + 1 (this has to satified, otheriwise, try the increased number)
#							if fifth step can be completed, THIS IS THE RIGHT NUMBER!

# def is_valid_total(total1):
# 	# step 1
# 	if total1 % 5 != 1:
# 		return False
# 	pile1 = (total1-1) // 5

# 	#step 2
# 	total2 = 4 * pile1
# 	if total2 % 5 != 1:
# 		return False
# 	pile2 = (total2-1) // 5

# 	#step 3
# 	total3 = 4 * pile2
# 	if total3 % 5 != 1:
# 		return False
# 	pile3 = (total3-1) // 5

# 	# step 4
# 	total4 = 4 * pile3
# 	if total4 % 5 != 1:
# 		return False
# 	pile4 = (total4 -1 ) // 5

# 	# step 5
# 	total5 = 4 * pile4
# 	if total5 % 5 != 1:
# 		return False
# 	pile5 = (total5-1) // 5
# 	if pile5 == 0:
# 		return False

# 	return True

def is_valid_total(number):
	total = number
	for i in range(5):
		if total % 5 != 1:
			return False
		pile = (total-1) // 5
		total = 4 * pile
	return True

total = 1
while not is_valid_total(total):
	total += 1

print(f"The first valid number is {total}")