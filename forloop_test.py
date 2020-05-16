# for from range
# for i in range(0, 100):
#     print(i, end=' ')

# for from list
# l = [1, 2, 3, 5, 4, 6]
# for i in l:
#     print(i, end=' ')

# tp = ("apple", "berry", "banana", "fox")
# for item in tp:
#     print (item, end=' ')

# st = {"grade1", "grade2", "grade3", "grade4"}
# for s in st:
#     print(s, end=' ')

dict_student = {"Bob": 10, "Abby": 8, "Delany": 5, "Smith": 13}
# for key in dict_student.keys():
#     print(key, end= ' ')
# for v in dict_student.values():
#     print (v, end= ' ')

# for k, v in dict_student.items():
#     print(f"k={k}, v={v}")

# for item in dict_student.items():
#     print(item, end=' ')

## nested for
for i in range(10):
    for j in range(10):
        print(i*j, end=' ')
    print()