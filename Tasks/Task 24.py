# 24. В заданном списке вещественных чисел найдите разницу между максимальным и минимальным значением дробной части элементов. 
# Пример: [1.1, 1.2, 3.1, 5, 10.01] => 0.19

spis = [1.110, 1.25, 3.255, 5, 10.011]
max = 0
min = spis[0] - int(spis[0])

for i in spis:
    if type(i) == type(5):
        i = float(i)
    drob = i - int(i)
    drob = round(drob, 5)
    if drob > max:
        max = drob
    else:
        continue

for i in spis:
    if type(i) == type(5):
        i = float(i)
    drob = i - int(i)
    drob = round(drob, 5)
    if drob > 0 :
        if drob < min:
            min = drob           
    else:
        continue
result = max-min
print(result)
