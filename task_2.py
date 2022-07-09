# Напишите программу для. проверки истинности утверждения 
# ¬(X ⋁ Y ⋁ Z) = ¬X ⋀ ¬Y ⋀ ¬Z для всех значений предикат.

r = range(2)
for x in r:
    for y in r:
        for z in r:
            print(f'Для значений x={x} y={y} z={z}')
            print('Утверждение', not(x or y or z) == ((not x) and (not y) and (not z)))
