dict_num = {}
list_digit = [0, 3, 3, 5, 4, 4, 3, 5, 5, 4]
list_teens = [3, 6, 6, 8, 8, 7, 7, 9, 8, 8 ]
list_tenth = [0, 3, 6, 6, 5, 5, 5, 7, 6, 6]

def count(num):
    hd3 = num // 100
    mod3 = num % 100
    global dict_num
    if hd3 > 0:
        if mod3 == 0:
            res = countHundreds(hd3)
        else:
            res = countHundreds(hd3) + 3 + dict_num[mod3]
    else:
        if mod3 < 10:
            res = countDigits(mod3)
        elif mod3 < 20:
            res = countTeens(mod3-10)
        else:
            th2 = num // 10
            mod2 = num % 10
            res = countTenths(th2) + countDigits(mod2)
    dict_num[num] = res
        


def countHundreds(hd):
    return list_digit[hd] + 7

def countTenths(th):
    return list_tenth[th]

def countTeens(tn):
    return list_teens[tn]

def countDigits(dt):
    return list_digit[dt]

for num in range(1, 1000):
    count(num)

print(sum(dict_num.values())+11)