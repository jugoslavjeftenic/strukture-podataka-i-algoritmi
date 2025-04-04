import os

os.system("cls")


def insert_sort(lista):
    sortirana_lista = [lista.pop(0)]

    while lista != []:
        for i in range(0, len(sortirana_lista)):
            if lista[0] < sortirana_lista[i]:
                sortirana_lista.insert(i, lista.pop(0))
                break
        else:
            sortirana_lista.append(lista.pop(0))

    return sortirana_lista


lista = [5, 6, 3, 2, 7, 0, 4]
print(lista)
print(insert_sort(lista))
