# 28. Подсчитать сумму цифр в числе

def SummNumbers(num):
    sum = 0
    for i in num:
        sum += int(i)
    return (f'Сумма цифр в числе {num} = {sum}')

print('Введите число: ')
print(SummNumbers(input()))