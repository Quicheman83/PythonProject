#t = [2, 7, 5, 6, 7, 1, 6, 2, 1, 7, 6]
t = [2, 55, 7, 55, 36, 7, 21, 56, 55, 3, 7, 6,2, 55, 7, 55, 36, 7, 21, 56, 55, 3, 7, 6,2, 55, 7, 55, 36, 7, 21, 56, 55, 3, 7, 6,2, 55, 7, 55, 36, 7, 21, 56, 55, 3, 7, 6,2, 55, 7, 55, 36, 7, 21, 56, 55, 3, 7]
a = []

if max(t) < len(t):
    z = len(t)
else: z = max(t)

for i in range(z + 1):
    a.append(0)

for i in t:
    a[i] = a[i] + 1
print(a)

ind = 0
max = 0
for i in range(len(a)):
    if a[i] > max:
        max = a[i]
        ind = i

u = []
for i in range(len(a)):
    if a[i] == max:
        u.append(i)


print(f"le numero le plus frequent est le {u} qui apparait {max} fois")





