# 11. Дано число из отрезка [10, 99]. Показать наибольшую цифру числа

import random
a = random.randint(10, 99)
print(f'Рандомное число = {a}')

def WhoMore(a):
    first_num = a // 10
    secont_num = a % 10

    if first_num > secont_num:
        return first_num
    else:
        return secont_num
print(f'наибольшая цифра = {WhoMore(a)}')   

# =========== 2 вариант решения ===========

import random
a = random.randint(10, 99)
print(f'Рандомное число = {a}')
def WhoMore2(num):   
    a = str(num)
    if a[0] > a[1]:
        return a[0]
    else:
        return a[1]
print(f'Наибольшая цифра из числа {a} это {WhoMore2(a)}')