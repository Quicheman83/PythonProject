a = int(input("prix/heure : "))
b = int(input("nb heure : "))
tt = 0

for i in range(b):
    if i <= 160 :
        tt = tt + a
    if i > 160 and i <= 200:
        tt = tt + a * 1.25
    if i > 200:
        tt = tt + a * 1.50

print(f"tarif : {tt}")