

n = int(input("entrer valeur"))
res = 1

b = int(input("entrer 1 pour while et 2 pour for"))

if b == 1:
    for i in range(1, n + 1):
        res = res * i
        print(res)
if b == 2:
    while (n > 0):
        res = res * n
        n = n - 1
        print(res)