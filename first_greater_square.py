#  Find the first square numbe that is greater than a given number
def first_greater_square(number):
# number = 1, 2, 3 => 4
# number = 4, 5, 6, 7, 8 => 9
# number = 9 => 16
# number = 111 => 121
# number 222 => 225

# algoritim is using while,
#   initialize index with 1
#   while loop
#       square the index, and compare with number, if the square is greater than number, then return the square
#       increase the index (otherwise, infinite loop)
    index = 1
    while True:
        square = index * index
        if square > number:
            return index, square
        index += 1

# print(first_greater_square(117))
import random
number = random.randint(1, 1000)
index, square = first_greater_square(number)
print(f"number: {number}, first greater index, square: {index}, {square}")