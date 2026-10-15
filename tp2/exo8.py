
appartient = False

x = int(input("entrer valeur : "))

if ((x > -10 or x == -10) and (x < -2 or x == -2)) or (x > 0 and (x < 1 or x == 1)) or ((x > 2 or x == 2) and x < 3):
    appartient = True

if appartient:
    print("x appartient à I")
else:
    print("x n'appartient pas à I")



#pour le quiz moodle


def tester(x):
    appartient = False

    if ((x > -10 or x == -10) and (x < -2 or x == -2)) or (x > 0 and (x < 1 or x == 1)) or (
            (x > 2 or x == 2) and x < 3):
        appartient = True

    if appartient:
        print("x appartient à I")
        return "in"
    else:
        print("x n'appartient pas à I")
        return "out"



l = [-2 , 0.1 , 4 , 1.5 , -1 , -9 , 3 , 1.2 , 2.9 , 0 , -20]

for i in l:
    print(tester(i))