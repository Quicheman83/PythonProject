
nombre = int(input("Entrez une nombre : "))

pair = "pair"
status = "positif"

if nombre == 0:
    print("Le nombre est zéro (et il est pair)")
else:
    if nombre < 0:
        status = "negatif"
    else:
        status = "positif"

    if nombre % 2 == 0:
        pair = "pair"
    else:
        pair = "impair"

    print(f"Le nombre est {status} et {pair}")