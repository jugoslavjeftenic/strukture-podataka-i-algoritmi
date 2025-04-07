import os

os.system("cls")


def bubble_sort_v2(niz):
    ima_promena = True

    while ima_promena:
        ima_promena = False

        for el in range(0, len(niz) - 1):
            if niz[el] > niz[el + 1]:
                niz[el], niz[el + 1] = niz[el + 1], niz[el]
                ima_promena = True

    return niz


niz = [5, 7, 1, 9, 6, 3, 2, 8, 4]
print(niz)
print(bubble_sort_v2(niz))
