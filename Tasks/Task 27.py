# 27. Строка содержит набор чисел. Показать большее и меньшее число. Символ-разделитель - пробел
string = '1 2 3 4 5 6'
string = string.replace(' ','')
strint_int = int(string)
result_max = max(string)
result_min = min(string)
print(result_max, result_min)

