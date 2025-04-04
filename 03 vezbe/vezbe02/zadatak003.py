import os

os.system("cls")


def selection_sort(lista):
    granica_idx = 0

    while granica_idx < len(lista):
        najmanji_idx = granica_idx

        for i in range(granica_idx + 1, len(lista)):
            if lista[najmanji_idx] > lista[i]:
                najmanji_idx = i

        lista[najmanji_idx], lista[granica_idx] = (
            lista[granica_idx],
            lista[najmanji_idx],
        )

        granica_idx += 1

    return lista


lista = [5, 6, 3, 2, 7, 0, 4]
print(lista)
print(selection_sort(lista))
