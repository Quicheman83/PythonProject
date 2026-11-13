from random import randint

a = randint(0,100)
essais = 1
z = -1

while z != a:
    z = int(input("entrer valeur : "))
    if z != a:
        if z < a:
            print("cest plus grand")
        elif z > a:
            print("cest plus petit")
        essais = essais + 1
print(f"gagné en {essais} essais.")



