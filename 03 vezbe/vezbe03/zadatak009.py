import os

os.system("cls")


def bubble_sort_v3(niz):
    ima_promena = True
    duzina_niza = len(niz)

    while ima_promena:
        ima_promena = False
        duzina_niza -= 1

        for el in range(0, duzina_niza):
            if niz[el] > niz[el + 1]:
                niz[el], niz[el + 1] = niz[el + 1], niz[el]
                ima_promena = True

    return niz


niz = [5, 7, 1, 9, 6, 3, 2, 8, 4]
print(niz)
print(bubble_sort_v3(niz))
