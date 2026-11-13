
x = int(input("enter valeur : "))
tab = []
tmp = 0


for i in range(x):
    tab.append(i)
    tmp = tmp + i
    if tmp == x:
        break

print(tab, x)
