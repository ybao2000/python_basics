name = 'Bobby'
age = 12
gender = True
height = "5'5\""

# print(height)

def print_info(name, age, height, gender):
    gb = 'Girl'
    if gender:
        gb = 'Boy'
    # print("My name is {0}. I am {1} year’s old, {2} tall. I am a {3}.".format(name, age, height, gb))
    print(f"My name is {name}. I am {age} year's old, {height} tall. I am a {gb}.")

print_info(name, age, height, gender)