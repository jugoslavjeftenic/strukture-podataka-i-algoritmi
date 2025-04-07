import os

os.system("cls")


def linearna_pretraga(niz, trazeni_element):
    for i in range(0, len(niz)):
        if trazeni_element == niz[i]:
            return i
    return -1


niz = [1, 2, 3, 4, 7, 8, 9, 12]
print(niz)
print(linearna_pretraga(niz, 9))
