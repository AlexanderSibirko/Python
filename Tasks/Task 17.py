# 17. Задать список из N элементов, заполненных числами из [-N, N]. 
# Найти произведение элементов на указанных позициях. Позиции хранятся в файле file.txt в одной строке одно число

import random

n = 11
spis = [i for i in range(-n,n+1)]
print(spis)

pos1 = random.randint(0,n*2)
pos2 = random.randint(0,n*2)

with open('file.txt', 'w') as data:
    data.write(f'{pos1}\n')
    data.write(f'{pos2}\n')

print(pos1,pos2)
print(f'элемент на позиции {pos1} это {spis[pos1]}')
print(f'элемент на позиции {pos2} это {spis[pos2]}')

proiz = 1
path = 'file.txt'
data = open(path, 'r')
for line in data:
    line_int = int(line)
    proiz *= spis[line_int]
data.close
print(proiz)