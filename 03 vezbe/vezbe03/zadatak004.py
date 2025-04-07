import os

os.system("cls")


def selection_sort_v2(niz):
    for granica in range(0, len(niz)):
        najmanji = granica

        for i in range(granica + 1, len(niz)):
            if niz[najmanji] > niz[i]:
                najmanji = i

        niz[granica], niz[najmanji] = niz[najmanji], niz[granica]

    return niz


niz = [5, 7, 1, 4, 6, 3, 2, 8]
print(niz)
print(selection_sort_v2(niz))
