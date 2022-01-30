# 8. Сообщить в какой четверти координатной плоскости или на какой оси находится точка с координатами Х и У 

def Chetvert():
    print('Введите координату X: ')
    x = int(input())
    print('Введите координату Y: ')
    y = int(input())
    if x == 0:
        if y == 0:
            return 'точка находится в начале координат'
        else:
            return 'точка находится на оси У'
    elif y == 0:
        if x == 0:
            return 'точка находится в начале координат'
        else:
            return 'точка находится на оси X'
    else:
        if x > 0:
            if y > 0:
                return '1 четверть'
            else:
                return '4 четверть'
        else:
            if y > 0:
                return '2 четверть'
            else:
                return '3 четверть'

print(Chetvert())