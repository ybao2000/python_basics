

def most_repeated_number(numbers):
    # first step: generate the dictionary
    dict_num = {}
    for number in numbers:
        if number in dict_num:
            # dict_num[number] += 1
            dict_num[number] = dict_num[number] + 1
        else:
            dict_num[number] = 1
    print(dict_num)

    # from the dictionary, find the key and value that has the biggest number
    kvp_result = ()
    for kvp in dict_num.items():
        if kvp_result:
            if kvp[1] > kvp_result[1]:
                kvp_result = kvp
        else:
            kvp_result = kvp
    return kvp_result[0]
    # print(key, value)


import random
numbers = []
for i in range(100):
    numbers.append(random.randint(1, 10))

print(numbers)
# most_repeated_number(numbers)
print(most_repeated_number(numbers))