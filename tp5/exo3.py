a = str(input("entrer mot ou phrase: "))
a = a.lower()
x = a.split(" ")
z = ""
pal = True

for i in x:
    z = z + i


for i in range(len(z) // 2):
    if not (z[i] == z[len(z) - 1 - i]):
        pal = False




print(f"palyndrome : {pal}")