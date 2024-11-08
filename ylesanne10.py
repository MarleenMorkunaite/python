# Harjutus 10
# 08.11.24 Marleen
import random
# 1. Arvude keskmine

# Koostage Pythoni programm, mis küsib kasutajalt arve ükshaaval. Programm peaks jätkama arvude küsimist ja nende vastuvõtmist seni, kuni kasutaja jätab sisestuse tühjaks (st vajutab sisestusklahvi ilma midagi kirjutamata).
# Programm peab kasutama while-tsüklit arvude küsimiseks ja nende salvestamiseks.
# Pärast seda, kui kasutaja lõpetab arvude sisestamise peab programm arvutama ja väljastama kõikide sisestatud arvude keskmise väärtuse.
'''
arvud = []
loop = 1

while loop==1:
    arv = input("Lisa arv: ")
    if arv=="":
        break
    arvud.append(int(arv))


print(sum(arvud)/len(arvud))
'''


# 2. Arvu äraarvamise mäng

# Kirjutage Pythoni skript, mis simuleerib arvu äraarvamise mängu.
# Programm peab esmalt genereerima juhusliku arvu vahemikus 1 -10.
# Seejärel küsib programm kasutajalt arve, püüdes ära arvata genereeritud arvu. Kasutaja jätkab arvude sisestamist, kuni ta arvab õige arvu ära. Iga kord, kui kasutaja sisestab arvu, peab programm andma tagasisidet, kas pakutud arv on õige või mitte.
# Pärast õige arvu äraarvamist teavitab programm kasutajat, mitmenda katsega õige arv ära arvati, ja küsib, kas kasutaja soovib mängida uuesti.
# Kui kasutaja vastab jaatavalt, genereerib programm uue juhusliku arvu ja mäng algab otsast peale.
# Kui kasutaja otsustab mitte jätkata, tänab programm kasutajat mängus osalemise eest ja kuvab kõik senised tulemused: mitmenda katsega igal korral õige arv ära arvati.
# Programm peab kasutama while-tsüklit nii arvude sisestamise protsessi juhtimiseks kui ka mängu kordamise otsustamiseks.

katsed = []
loop = 1
arvamused = 0
suv = random.randint(1,10)
print(suv)

while loop==1:
    arv = int(input("Arva arv 1-10: "))
    arvamused+=1
if arva == suv:
    print("Õige")
    print(f"Proovimisi (arvamused) korda!")
    katsed.append(arvamused)
    uuesti = input("Soovid uuesti? (j/e)")
    if uuesti=="j":
        suv = random.randint(1,10)
        arvamused = 0
    else: 
        break
else:
    print("Proovi uuesti!")
print("Gameover")
print(arvamused)