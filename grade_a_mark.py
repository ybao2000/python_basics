import random
def grade_a_mark(mark):
    if mark >= 95:
        return "A+"
    elif mark >= 90:
        return "A"
    elif mark >= 85:
        return "A-"
    elif mark >= 80:
        return "B+"
    elif mark >= 75:
        return "B"
    elif mark >= 70:
        return "B-"
    elif mark >= 65:
        return "C+"
    elif mark >= 60:
        return "C"
    elif mark >= 55:
        return "C-"
    elif mark >= 50:
        return "D"
    else:
        return "F"

# print(grade_a_mark(72))
mark = random.randint(0, 100)
print(f"mark is {mark}, grade is {grade_a_mark(mark)}")