# randomly given a number between 1 and 10, 
# keep guessing the number by input until correct

import random

num = random.randint(1, 50)
while True:
	guess = input("enter a number: ")	# input is reading a string from keyboard
	if guess.isdigit():		# make sure the string is a number
		iGuess = int(guess)	# convet the string to number
		if iGuess == num:
			print(f"Bingo...you got the right number {num}")
			break
		elif iGuess > num:
			print("You number is too high...try another guess")
		else: 
			print("Your number is too low...try another guess")
	else:
		print("You brat... you need to enter a number")
