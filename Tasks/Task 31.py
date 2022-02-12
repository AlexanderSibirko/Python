# 31. Составить список простых множителей натурального числа N
def Factor(n):
    Ans = []
    d = 2
    while d * d <= n:
        if n % d == 0:
            Ans.append(d)
            n //= d
            print('1')
        else:
            d += 1
            print('2')
    if n > 1:
        Ans.append(n)
        print('3')
    return Ans
print(Factor(29))

