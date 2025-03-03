import os; os.system("cls")

def moj_sort(lista):
    nesortirano = lista
    sortirano = []

    while nesortirano != []:
        najmanji = nesortirano[0]

        for n in range(1, len(nesortirano)):
            if najmanji > nesortirano[n]:
                najmanji = nesortirano[n]

        sortirano.append(najmanji)
        nesortirano.remove(najmanji)

    return sortirano

lista = [5, 6, 3, 2, 7, 0]
print(lista)
print(moj_sort(lista))
