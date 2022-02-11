# 25. Написать программу преобразования десятичного числа в двоичное

# num = 222
# n = 56
# result = []
# while n >= 0:
#     if num >= 2**n:
#         num = num % 2**n
#         result.append(1)
#     else:
#         if result == []:
#             result.clear
#         else:
#             result.append(0)   
#     n -= 1

# print(result)

# ИЛИ
num = 222
result = bin(num)
print(result)