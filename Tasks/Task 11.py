# 11. Для натурального N создать список: 1, -3, 9, -27, 81 и т.д.

def Spisok():
    spisok = []
    print('Введите число N: ')
    n = int(input())
    i = 0
    x = 3
    while i <= n:
        if i % 2 == 0:
            spisok.append(x**i)
        else:
            spisok.append(-(x**i))
        i += 1
    return spisok

print(Spisok())
