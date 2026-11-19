t = [5, 2, 4, 8, 1, 3]
ind = 0
for i in range(len(t)):
    a = ind
    x = t[ind]
    z = ind
    print(f"for {ind}, {len(t)}")
    for j in range(ind, len(t)):
        print(f"comp {t[j]} < {x}")
        if t[j] < x :
            x = t[j]
            z = j
    print(t[a], t[z])
    t[a], t[z] = t[z], t[a]
    ind+=1
print(t)

