tt = 0
div = 0

for i in range(5):
    a = str(input("entrer note et coef ex: '10.5 2' :"))
    x = a.split(" ")
    tt = tt + float(x[0]) * int(x[1])
    div = div + int(x[1])

print(f"moyenne {tt/div}")