import os; os.system("cls")

# O(1) konstantna slozenost
def ispis1():
    print("A")

# O(n) linearna slozenost
def ispis2(n):
    for i in range(n):
        print(i)

# O(n^2) kvadratna slozenost
def ispis3(n):
    for i in range(n):
        for j in range (n):
            print(i)

# O(1)
def ispis4():
    print("A")
    print("B")

# O(n)
def ispis5(n):
    for i in range(n):
        print(i)
        print(i + 1)

# O(n^2)
def ispis6(n):
    for i in range(n):
        for j in range (n):
            print(i)
            print(j)

ispis1()
ispis2(20)
ispis3(20)
ispis4()
ispis5(20)
ispis6(20)
