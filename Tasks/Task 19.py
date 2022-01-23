# 19. Определить номер четверти плоскости, в которой находится точка с координатами Х и У, причем X ≠ 0 и Y ≠ 0

def NumberChetvert(x,y):
    print(f'\n Координата х = {x}\n')
    print(f' Координата y = {y}\n')
    if (x > 0) and (y > 0):
        return 1
    elif ((x < 0) and (y > 0)):
        return 2
    elif ((x < 0) and (y < 0)):
        return 3
    elif ((x > 0) and (y < 0)):
        return 4
print(f'Точка находится в {NumberChetvert(-2,-3)} четверти\n')