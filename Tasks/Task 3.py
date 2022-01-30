# 3. Вывести на экран числа от -N до N

def OtNdoN(num):
    i = -num
    result = []
    while i <= num:
        result.append(i)
        i += 1
    return result
print(OtNdoN(12))