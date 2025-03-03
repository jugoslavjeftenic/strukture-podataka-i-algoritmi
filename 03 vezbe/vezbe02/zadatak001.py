import os; os.system("cls")

def nadji_najmanji(lista):
    ret_val = lista[0]
    for n in lista:
        if ret_val > n:
            ret_val = n
    return ret_val

def nadji_indeks_najmanjeg(lista):
    ret_val = 0
    for n in range(1, len(lista)):
        if lista[ret_val] > lista[n]:
            ret_val = n
    return ret_val

def nadji_indeks_i_vrednost_najmanjeg(lista):
    indeks = 0
    for n in range(1, len(lista)):
        if lista[indeks] > lista[n]:
            indeks = n
    return indeks, lista[indeks]

lista = [5, 2, 6, 4, 10, 1]
print(nadji_najmanji(lista))
print(nadji_indeks_najmanjeg(lista))
print(nadji_indeks_i_vrednost_najmanjeg(lista))
