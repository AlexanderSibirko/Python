# 7. Проверить истинность утверждения ¬(X ⋁ Y ⋁ Z) = ¬X ⋀ ¬Y ⋀ ¬Z для всех значений предикат

X = False
Y = False
Z = False
l = not(X or Y or Z)
r = not X and not Y and not Z
print(l == r)