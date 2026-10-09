
m = int(input("entrer minutes :"))

j = m//(1440)
m = m - j*(1440)
h = m//(60)
m = m - h*(60)


print(f"il reste : j{j}:h{h}:m{m}")