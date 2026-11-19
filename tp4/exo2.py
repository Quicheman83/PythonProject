
nb_etu = int(input("donner nb etudiant"))
moyenne = 0.0
tt = 0.0

notes = []
for i in range(nb_etu):
    x = float(input("entrer note"))
    while x < 0 or x > 20:
        x = float(input("enter note"))
    tt = tt +x
    notes.append(x)

moyenne = tt/nb_etu

print(f"moyenne {moyenne}")
for i in range(len(notes)):
    print(f"{i} | {notes[i]} | {notes[i] - moyenne}")


