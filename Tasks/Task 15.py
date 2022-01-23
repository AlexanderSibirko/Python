# 15. Дано число. Проверить кратно ли оно 7 и 23

import random
a = random.randint(1, 99)
print(f'Рандомное число = {a}')
if a % 23 == 0:
    print(f'число {a} кратно 23')
elif a % 7 == 0:
    print(f'число {a} кратно 7')
else:
    print(f'число {a} не кратно ни 7, ни 23')
