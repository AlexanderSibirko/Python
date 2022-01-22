# import random
# a = random.randint(1, 22)
# print(a)

# 11. Дано число из отрезка [10, 99]. Показать наибольшую цифру числа
# import random
# a = random.randint(1, 99)
# print(f'Рандомное число = {a}')
# first_num = a // 10
# secont_num = a % 10

# if first_num > secont_num:
#     print(f'наибольшая цифра = {first_num}')
# else:
#     print(f'наибольшая цифра = {secont_num}')

# 15. Дано число. Проверить кратно ли оно 7 и 23

# import random
# a = random.randint(1, 99)
# print(f'Рандомное число = {a}')
# if a % 23 == 0:
#     print(f'число {a} кратно 23')
# elif a % 7 == 0:
#     print(f'число {a} кратно 7')
# else:
#     print(f'число {a} не кратно ни 7, ни 23')


# 21. Программа проверяет пятизначное число на палиндромом
# print('Введите пятизначное число')
# num = input()
# numstr = str(num)
# if numstr[0] == numstr[4]:
#     if numstr[1] == numstr[3]:
#         print('Введенное число является палидромом')
#     else:
#         print(f'Число {num} не палиндром!')
# else:
#     print(f'Число {num} не палиндром!')

# 19. Определить номер четверти плоскости, в которой находится точка с координатами Х и У, причем X ≠ 0 и Y ≠ 0
# x = 5
# print(f' Координата х = {x}')
# y = -3
# print(f' Координата y = {y}')
# if (x > 0) and (y > 0):
#     print('Точка находится в 1 четверти')
# elif ((x < 0) and (y > 0)):
#     print('Точка находится во 2 четверти')
# elif ((x < 0) and (y < 0)):
#     print('Точка находится в 3 четверти')
# elif ((x > 0) and (y < 0)):
#     print('Точка находится в 4 четверти')

