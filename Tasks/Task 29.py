# 29. Написать программу вычисления произведения чисел от 1 до N

def ProizvedDoN(num):
    num = int(num)
    proiz = 1
    count = 1
    while count <= num:
        proiz *= count
        count += 1
    return (f'Произведение чисел от 1 до {num} = {proiz}')

print('Введите число N: ')
print(ProizvedDoN(input()))
