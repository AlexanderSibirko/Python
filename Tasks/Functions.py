# ====================== ПОЛЕЗНЫЕ ФУНКЦИИ =====================

def Summator(*params):                 # Суммирует все введенные параметры, сколько захотим
    res = 0
    for item in params:
        res += item
    return res


import random
def RandomNum():
    a = random.randint(1, 10)
    print(f'Рандомное число = {a}')


def fib(n):
    if n in [1, 2]:
        return 1
    else:
        return fib(n-1) + fib(n-2)

def fibbonachi(n):
    list = []
    for e in range(1, n):
        list.append(fib(e))
    return list





# r = open('file.txt', 'w')
# r.write('каждый охотник желает знать где сидит фазан')
# r.close()

