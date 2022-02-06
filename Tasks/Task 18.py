# 18. Реализовать алгоритм перемешивания списка. 

from random import randint


spis = [i for i in range(0,21)]
spis2 = []

print(spis)
for i in range(0, len(spis)-1):
    random = randint(i, len(spis)-1)
    spis[i], spis[random] = spis[random], spis[i]

print(spis)
