# 21. Программа проверяет пятизначное число на палиндромом

def PolindromOrNo(num):
    
    numstr = str(num)
    if numstr[0] == numstr[4]:
        if numstr[1] == numstr[3]:
            return 'Введенное число является палидромом'
    else:
        return (f'Число {num} не палиндром!')
print('Введите пятизначное число')
print(PolindromOrNo(input()))