# 16. Задать список из n чисел последовательности (1+1/n)^n и вывести на экран их сумму

sum = 0
x = 0
n= int(input('Введите число N: '))
spis = []
for i in range(1,n+1):
    x = round((1+1/i)**i, 3)

    spis.append(x)
    sum += x
print (spis)
print(f'сумма равна {sum}')