
def a():
    print(f"x1:{x1} x2:{x2} x3:{x3}")

for i in range(3):
    if i == 0:
        x1, x2, x3 = 5, 8, 2

    if i == 1:
        x1, x2, x3 = 3, 3, 9

    if i == 2:
        x1, x2, x3 = 5, 3, 7

    print("==========================================")

    print(not(x1 == x2) and not (x1 == x2))
    print((x1 > x2) or (x3 < x1))
    print((x1 < x2) and (x2 < x3))
    print(not((x1 > x2) and (x1 < x3)))
    print((x1 == x2) or (x3 == x1) or (x2 == x3))

