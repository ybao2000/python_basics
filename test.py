####### basic data type
# string
# number: int, float
# boolean

#######operators
# +, -, *, /, //, %, ** (math)
# >, <, >=, <=, <>, == (comparison)
# and, or, not (logic)
# = (assign)

##########collection (iterable)
# tuple (), (1, 2, 3, 4, 5), index
# list [], [1, 2, 3, 4, 5, 5], index
# set {}, {1, 2, 3, 4, 5} item, unique
# dictionary {'apple': 3, 'peach': 4, 'banana': 5} kvp=> key value pair, key is unique

############if
# if condition1:
#    	do something
# elif condition2:
#     do something
# elif condiction3:
#     do something
# else: (optional)
#     do something (pass if don't anything)

############loop
###for - fixed loop
# for variable in collection(iterable) => range(start, end, increment) => generate a collection
#    do something
#    break 
# else:
#    do something
### while condition (if condition never fails, then infinite looooooooooooooooooooooop)
#		do something

# i = 0
# while i < 100:
# 	print(i)
# 	# i += 1

# def sum(num1, num2):
# 	return num1+num2+5

# print(sum(1, 2))
# t = (1, 2, 3)
# print(t)
# s ={1, 3, 4, 5}
# print(s)

# print(1,2,3,4, sep='#', end='***')
# print(1,2,3,4, sep='')

### str => convert any object into string
# a = 1111
# b = True
# c = str(b)
# print(a, b, c)

#### int => convert string to int
# a = '11122'
# b = int(a)
# print(b+3)

####input function => get string from your keyboard
# a = input("Input your name: ")
# print("your name is " + a)
# age = int(input("Input your age: "))
# # print("your age is " + str(age))
# print(f"Your age is {age}")

# import math
# print(math.pi)
# print(math.e)
# print(math.sqrt(12*12+5*5))

import random # math and random are built-in module (means, you don't have to install it)
print(random.randint(1, 5))	# return any number between 1 and 5 (1, and 5 inclued)