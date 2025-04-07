import os

os.system("cls")


def binarna_pretraga(niz, trazeni_element):
    pocetak = 0
    kraj = len(niz) - 1

    while pocetak <= kraj:
        indeks = (pocetak + kraj) // 2

        if trazeni_element > niz[indeks]:
            pocetak = indeks + 1
        elif trazeni_element < niz[indeks]:
            kraj = indeks - 1
        else:
            return indeks

    return -1


niz = [1, 2, 3, 4, 7, 8, 9, 12]
print(niz)
print(binarna_pretraga(niz, 6))
