# 19.11.24 Marleen
# harjutus 14

# Loo programm, mis võimaldab kasutajatel hiire abil joonistada kujundeid (vali ise ruut, ring, kolmnurk vms) ekraanile ning muuta joonistusvärvi klaviatuuri abil.
# Kasutajad peaksid saama kasutada hiire vasakut nuppu joonistamiseks ja paremat nuppu joonistatud elementide kustutamiseks.
# Klaviatuuri klahvid ‘R’, ‘G’ ja ‘B’ võimaldavad vastavalt värvi muuta punaseks, roheliseks või siniseks.


import turtle
ekraan = turtle.Screen()

def muuda_varvi_red():
    turtle.color("red")

def muuda_varvi_green():
    turtle.color("green")

def muuda_varvi_blue():
    turtle.color("blue")


def ruut(x,y):
    print(x,y)
    turtle.speed(0)
    turtle.penup()
    turtle.goto(x, y)
    turtle.pendown()
    for i in range(4):
        turtle.fd(50)
        turtle.left(90)



def puhasta_ekraan(x, y):
    turtle.clear()



ekraan.onscreenclick(ruut, 1) # Vasak klõps
ekraan.onscreenclick(puhasta_ekraan, 3) # Parem klõps

ekraan.onkey(muuda_varvi_red, "r")
ekraan.onkey(muuda_varvi_green, "g")
ekraan.onkey(muuda_varvi_blue, "b")
ekraan.listen()


turtle.mainloop()
