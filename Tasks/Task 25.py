# 25. Найти сумму чисел от 1 до А
n = int(input('Введите число A: '))
sum = 0
count = 1
while count <= n:
    sum += count
    print(count)
    count += 1
print(f'Сумма чисел от 1 до А = {sum}')
