import os

os.system("cls")


def selection_sort_v1(niz):
    granica = 0
    while granica < len(niz):
        najmanji = granica

        for i in range(granica + 1, len(niz)):
            if niz[najmanji] > niz[i]:
                najmanji = i

        niz[granica], niz[najmanji] = niz[najmanji], niz[granica]
        granica += 1

    return niz


niz = [5, 7, 1, 4, 6, 3, 2, 8]
print(niz)
print(selection_sort_v1(niz))
