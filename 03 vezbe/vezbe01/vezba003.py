import os; os.system("cls")

def brute_force(trazena_lozinka):
    znakovi = "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ!@#$%^&*()-_=+"
    for z1 in znakovi:
        for z2 in znakovi:
            for z3 in znakovi:
                for z4 in znakovi:
                    for z5 in znakovi:
                        trenutni_pokusaj = z1 + z2 + z3 + z4 + z5
                        if trenutni_pokusaj == trazena_lozinka:
                            print(f"Lozinka je: {trenutni_pokusaj}")
                            return

# O(n^5) polinomska slozenost
brute_force("aaaaa")
# brute_force("spasp")
