# 24.10.24 Marleen
# Harjutus 9
import random

# Genereeri ja kuva arvud arvud 1-20

for i in range (1,21):
    print(i,end=" ")
print()



# Genereeri ja kuva 20 suvalist arvu vahemikus 1-99

for i in range (1,99):
    print(random.randint(1,99))


# Kasuta loendit 60, 5, 4, 42, 99, 67, 47, 22, 34, 8, 85, 50, 94, 39, 54, 83, 27, 40, 17, 75
#   Leia paaris ja paaritud arvud ning lisa oma loendisse
#   Kuva paaris ja paritute arvude summad

loend = [60, 5, 4, 42, 99, 67, 47, 22, 34, 8, 85, 50, 94, 39, 54, 83, 27, 40, 17, 75]
paaris = []
paaritu = []
for i in loend:
    if i%2==0:
        paaris.append(i)
    else:
        paaritu.append(i)


print("paaris arvude summa",sum(paaris))
print("paaritu arvude summa",sum(paaritu))



# Kuva arvud 1-42
#  Arvud, mis jagunevad 3, lisa tekst TIK (näiteks 3 TIK)
#  Arvud, mis jagunevad 5, lisa tekst TAK (näiteks 5 TAK)
#  Kui jagunevad mõlemaga, siis lisa tekst TIKTAK (näiteks 15 TIKTAK)

for i range(1,43):
    if i%3==0:
print(i, "TIK", end=" ")
elif i%5==0:
print(i, "TAK", end=" ")








# Leia kõik arvud vahemikus 200 kuni 320, mis jaguvad 7-ga, kuid ei jagu 5-ga. Prindi need arvud komadega eraldatult ühele reale