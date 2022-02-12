# 29. Найти НОК двух чисел

def NOD(a,b):
    while(b>0):
        a,b=b,a%b
    return a
print(NOD(2,7))

def NOK(x,y):
    return (x*y)//NOD(x,y)

print(NOK(2,7))



