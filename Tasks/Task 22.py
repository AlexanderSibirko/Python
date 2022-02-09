# . 22. Найти сумму чисел списка стоящих на нечетной позиции

spis = list(range(0,11))
print(spis)
def SummNechet(spis):
    result = 0
    for i in spis:
        i_int = int(i)
        if i_int % 2 == 1:
            result += i_int
        else:
            continue
    return result

print(SummNechet(spis))