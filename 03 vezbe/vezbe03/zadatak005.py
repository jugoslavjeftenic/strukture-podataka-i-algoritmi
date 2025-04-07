import os

os.system("cls")


def insertion_sort_v1(niz):
    granica = 1

    while granica < len(niz):
        zameni = granica - 1

        while zameni >= 0 and niz[zameni + 1] < niz[zameni]:
            niz[zameni + 1], niz[zameni] = niz[zameni], niz[zameni + 1]
            zameni -= 1

        granica += 1

    return niz


niz = [5, 7, 1, 4, 6, 3, 2, 8]
print(niz)
print(insertion_sort_v1(niz))
