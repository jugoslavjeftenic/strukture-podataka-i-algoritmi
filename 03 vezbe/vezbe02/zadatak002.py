import os

os.system("cls")


def selection_sort(lista):
    sortirana_lista = []

    while lista != []:
        najmanji = lista[0]

        for n in range(1, len(lista)):
            if najmanji > lista[n]:
                najmanji = lista[n]

        sortirana_lista.append(najmanji)
        lista.remove(najmanji)

    return sortirana_lista


lista = [5, 6, 3, 2, 7, 0, 4]
print(lista)
print(selection_sort(lista))
