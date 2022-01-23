# 21. Программа проверяет пятизначное число на палиндромом

print('Введите пятизначное число')
num = input()
numstr = str(num)
if numstr[0] == numstr[4]:
    if numstr[1] == numstr[3]:
        print('Введенное число является палидромом')
    else:
        print(f'Число {num} не палиндром!')
else:
    print(f'Число {num} не палиндром!')