# 19. Реализовать алгоритм задания случайных чисел. Без использования встроенного генератора псевдослучайных чисел


set_ = set()
for i in range(0,11):
    set_.add((str(i)))     
    
list = []
for i in set_:
    iint = int(i)
    list.append(iint)
print(list)