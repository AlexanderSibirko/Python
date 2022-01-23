# 25. Найти сумму чисел от 1 до А

def Summa(num):
    n = int(num)
    sum = 0
    count = 1
    while count <= n:
        sum += count
        count += 1
    return (f'Сумма чисел от 1 до {num} = {sum}')

print('Введите число А: ')
print(Summa(input()))