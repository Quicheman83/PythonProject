#ex3
tt = 0

j = int(input("entrer jour :"))
h = int(input("enter heure :"))
m = int(input("enter minute :"))

j_r = 31 - j
h_r = 24 - h
m_r = 60 - m

tt = tt + j_r * 24 * 60 + h_r * 60 + m_r
print(tt)