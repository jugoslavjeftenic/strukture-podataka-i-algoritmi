import os

os.system("cls")


def insert_sort(lista):
    for i in range(1, len(lista)):
        for j in range(0, i):
            if lista[i] < lista[j]:
                lista.insert(j, lista.pop(i))
                break

    return lista


lista = [5, 6, 3, 2, 7, 0, 4]
print(lista)
print(insert_sort(lista))
