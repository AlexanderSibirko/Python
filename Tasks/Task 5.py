# 5. Дано число. Проверить кратно ли оно 5 и 10 или 15 но не 30

from cgitb import reset
from unittest import result


def Kratnost(num):
    if num % 5 == 0:
        if num % 10 == 0:
            if num % 30 != 0:
                return 'Заданное число кратно 5 и 10, но не кратно 30'
            else:
                return 'Заданное число кратно 5, 10, и 30'
        elif num % 15 == 0:
            if num % 30 != 0:
                return 'Заданное число кратно 5 и 15, но не кратно 30'
            else:
                return 'Заданное число кратно 5, 15, и 30'
        else:
            return 'Заданное число кратно 5, но не кратно ни 10 ни 15, и тем более 30'
    else:
        return 'Заданное число не кратно даже 5 и тем более 10 и 30'

print(Kratnost(45))