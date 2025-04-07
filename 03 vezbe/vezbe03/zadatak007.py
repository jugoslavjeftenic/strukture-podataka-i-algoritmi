import os

os.system("cls")


def bubble_sort_v1(niz):
    for i in range(0, len(niz)):
        for el in range(0, len(niz) - 1 - i):
            if niz[el] > niz[el + 1]:
                niz[el], niz[el + 1] = niz[el + 1], niz[el]

    return niz


niz = [5, 7, 1, 9, 6, 3, 2, 8, 4]
print(niz)
print(bubble_sort_v1(niz))
