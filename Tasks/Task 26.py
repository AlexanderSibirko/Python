# 26. Дано число. Составить список чисел Фибоначчи, в том числе для отрицательных индексов. 
# Т е для k = 8, список будет выглядеть так: [-21 ,13, -8, 5, −3,  2, −1,  1, 0, 1, 1, 2, 3, 5, 8, 13, 21] Негафибоначчи

# num = 8

# a = 0
# b = 1
# result = [a,b]
# while len(result) <= num:
#     a, b = b, a+b
#     result.append(b)

# if num % 2 == 0:
#     a,b = -b,a
# else:
#     a,b = b,-a
# result2 = [a, b]

# while len(result2) <= num*2:
#     a,b = b, a+b
#     result2.append(b) 

# print(result2)