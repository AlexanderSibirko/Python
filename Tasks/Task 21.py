# 21. Определить, позицию второго вхождения строки в списке либо сообщить, что её нет.

spis =  ["qwe", "asd", "zxc", "qwe", "ertqwe"]        
num = 'qwe'
def Position2(spis, num):

    if spis.count(num) > 1 :
        return spis.index(num,2)
    else:
        return -1
print(Position2(spis,num))
