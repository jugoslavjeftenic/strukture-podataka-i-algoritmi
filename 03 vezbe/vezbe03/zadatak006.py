import os

os.system("cls")


def insertion_sort_v2(niz):
    for granica in range(1, len(niz)):
        for i in range(granica, 0, -1):
            if niz[i] < niz[i - 1]:
                niz[i], niz[i - 1] = niz[i - 1], niz[i]
            else:
                break

    return niz


niz = [5, 7, 1, 4, 6, 3, 2, 8]
print(niz)
print(insertion_sort_v2(niz))
