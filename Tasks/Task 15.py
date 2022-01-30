# 15. Написать программу получающую набор произведений чисел от 1 до N.
# Пример: пусть N = 4, тогда
# [ 1, 2, 6, 24 ]

def Program():
    num = int(input('Введите число N: '))
    result = []
    i=1
    while i <= num:
        if i == 1:
            result.append(1)
        else:
            result.append(i*result[i-2])
        i += 1
    return result

print(Program())        