import os; os.system("cls")

class Student:
    def __init__(self, ime, prezime, ocene):
        self.ime = ime
        self.prezime = prezime
        self.ocene = ocene

    def predstavi_se(self):
        print(f"Ja sam student {self.ime} {self.prezime}")
    
    def izracunaj_prosek(self):
        suma = 0
        for ocena in self.ocene:
            suma += ocena
        print(suma / len(self.ocene))

pera = Student("Pera", "Peric", [10, 6, 9, 10])
maja = Student("Maja", "Majic", [10, 10, 10, 10])

pera.predstavi_se()
pera.izracunaj_prosek()

print(maja.ime)
print(maja.prezime)
print(maja.ocene)
