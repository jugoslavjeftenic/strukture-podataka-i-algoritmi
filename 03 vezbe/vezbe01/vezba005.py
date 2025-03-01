import os; os.system("cls")

# O(n) linearna slozenost
lista = [5, 6, 8, 4, 2]
for element in lista:
    if element % 2 == 0:
        element /= 2
    else:
        element *= 3
        element += 1
