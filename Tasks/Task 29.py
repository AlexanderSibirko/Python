# 29. Написать программу вычисления произведения чисел от 1 до N
n = int(input('Введите число N: '))
proiz = 1
count = 1
while count <= n:
    proiz *= count
    print(count)
    count += 1
print(f'Произведение чисел от 1 до N = {proiz}')