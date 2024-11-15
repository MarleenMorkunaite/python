# 15.11 Marleen
# Harjutus 11

import turtle
import random

# Kilpkonn – kirjutada programm, mis lubab kasutajal valida kujundite tüübi (viisnurk, ring, ruut või suvaline) ja arvu. Programm joonistab seejärel antud arvu kujundeid valitud tüübiga või juhul, kui valik on “suvaline”, valib programm ise juhuslikult kujundi tüübi iga kujundi jaoks.
# Millist kujundit soovid joonistada (viisnurk, ring, ruut, suvaline)? Suvaline
# Mitu kujundit soovid joonistada? 5

def viisnurk(k):
    print("Joonistan viisnurga")




def ring(k):
    print("Joonistan ringi")




def ruut(k):
    turtle.speed(0)
    for j in range(k):
        turtle.penup()
        turtle.goto(random.randint(-400,400),random.randint(-400,400))
        turtle.pendown()
        turtle.rt(random.randint(0,90))
        for i in range(4):
            turtle.fd(100)
            turtle.lt(90)

def suvaline(k):
    for i in range(k):
        my_list = [viisnurk, ring, ruut]
        random.choice(my_list)(1)

    



print("-------------------Minu programm--------------")


loop = 1

while loop==1:
    try:
        valik = int(input("1- viisnurk\n2 - ring\n3 - ruut\n4 - suvaline\nLisa valik (1-4): "))
        kujunditeArv = int(input("Mitu kujundit soovid joonistada? "))
    except: 
        print("Game over")
        turtle.bye()
        loop = 0
        break
    if valik=="" or kujunditeArv=="":
        print("Game over")
        turtle.bye()
        loop = 0
        break

    if valik == 1:
        viisnurk(kujunditeArv)
    if valik == 2:
        ring(kujunditeArv)
    if valik == 3:
        ruut(kujunditeArv)
    else:
        suvaline(kujunditeArv)









# Kirjuta funktsioon, mis kontrollib, kas kahest sõnast koosnev sõne algab sama tähega.
'''
def sarnased_esitahed(nimi):
    tykk = nimi.split(" ")
    if tykk[1][0] == tykk[1][0]:
        return True
    else:
        return False



print(sarnased_esitahed('Vapper Vares')) # peaks tagastama True
print(sarnased_esitahed('Lahe Känguru')) # peaks tagastama False
'''

# Kirjuta funktsioon nimega kolm_pikimat_sona(), mis analüüsib sõnade listi ja leiab kolm kõige pikemat sõna. Lisa kontroll juhuks, kui sõnade arv pole piisav.
'''
def kolm_pikimat_sona(a):
    sonastik = {}
    for i in a:
        sonastik[i]= len(i)
    sorteeritud = sorted(sonastik.items(), key = lambda x:x[1], reverse = True)
    for j in range(3):
        print(sorteeritud[j][0])


sonad = ["üks", "kaks", "viis", "kolmsada", "üksmiljonsadamust"]

kolm_pikimat_sona(sonad)
'''

turtle.done()