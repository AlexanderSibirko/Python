# 10. Найти расстояние между двумя точками пространства

from cmath import sqrt
import math

a = [2,3,4]
b = [3,5,8]
rasstoyanie = math.sqrt((b[0]-a[0])**2 +(b[1]-a[1])**2+(b[2]-a[2])**2 )
print(rasstoyanie)