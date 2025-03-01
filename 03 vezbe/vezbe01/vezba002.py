import os; os.system("cls")

def odstampaj_prvi(lista):
    print(lista[0])

# O(1) konstantna slozenost
# odstampaj_prvi([5, 6, 7, 8, 2, 5])

def saberi_i_odstampaj(lista):
    suma = 0
    for element in lista:
        suma += element
    print(suma)

# O(n) linearna slozenost
# saberi_i_odstampaj([5, 6, 7, 8, 3, 6])

# def odstampaj_tablicu_mnozenja(n):
#     for prvi in range(1, n+1):
#         for drugi in range(1, n+1):
#             if drugi >= prvi:
#                 print(f"{prvi} * {drugi} = {prvi * drugi}")
def odstampaj_tablicu_mnozenja(n):
    for prvi in range(1, n+1):
        for drugi in range(prvi, n+1):
            print(f"{prvi} * {drugi} = {prvi * drugi}")

# O(n^2) kvadratna slozenost
odstampaj_tablicu_mnozenja(8)
