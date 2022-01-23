# 15. Дано число. Проверить кратно ли оно 7 и 23

import random

def KratOrNo(num_1, num_2):
    a = random.randint(1, 99)
    print(f'Рандомное число = {a}')
    if a % num_2 == 0:
        print(f'число {a} кратно {num_2}')
    elif a % num_1 == 0:
        print(f'число {a} кратно {num_1}')
    else:
        print(f'число {a} не кратно ни {num_1}, ни {num_2}')
KratOrNo(7,23)