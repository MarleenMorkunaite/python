# 19.11.24 Marleen
# Harjutus 15

# Pane tööle eespool kirjeldatud ringi ja ristküliku liikumine
# Täienda koodi selliselt, et ring puudub ristkülikut, saab mängija punkti (kuvatakse ekraanil)
# Täienda koodi nii, et kui ring puudub alumist akna äärt, siis mäng lõpetatakse
# Täienda mängu nii, et kui ring puudub ristkülikut, siis see põrkab tagasi
# Lisa mängule mingi raskusaste – edasi mängides muudetakse näiteks palli ja ristküliku kiirusi.



import turtle
import random

aken = turtle.Screen()
aken.bgcolor("lightblue")
aken.setup(width=600, height=600)
aken.tracer(0)

# ristkülik
ristkylik = turtle.Turtle()
ristkylik.shape("square")
ristkylik.shapesize(stretch_wid=1, stretch_len=5)
ristkylik.penup()
ristkylik.color("black")
ristkylik.goto(ristkylik.xcor(), -250)

# ring
ring = turtle.Turtle()
ring.shape("circle")
ring.penup()
ring.speed('fastest')
ring.setheading(random.randint(0, 360))

# kiirused
ristkyliku_kiirus = 20
kiirus = 10



# ristküliku funktsioonid
def liigu_vasakule():
    x = ristkylik.xcor()
    if x > -280:
        ristkylik.setx(x - ristkyliku_kiirus)

def liigu_paremale():
    x = ristkylik.xcor()
    if x < 280:
        ristkylik.setx(x + ristkyliku_kiirus)

# ringi funktsioonid
def peegelda_porkumisel():
    nurk = ring.heading()
    if ring.xcor() >= 300 or ring.xcor() <= -300:
        uus_nurk = 180 - nurk
    if uus_nurk < 0:
        uus_nurk += 36
        ring.setheading(uus_nurk)
        if ring.ycor() >= 300 or ring.ycor() <= -300:
            uus_nurk = 360 - nurk
            ring.setheading(uus_nurk)


def tuvasta_kokkuporge():
    if ring.ycor() <= -250 and ring.ycor() == ristkylik.xcor():
    global skoor
    skoor = 1
    print(f"skoor: (skoor)")

    print("pihtas")


def ring_liigu():
    ring.forward(kiirus)
    peegelda_porkumisel()
    tuvasta_kokkuporge()
    aken.update()
    aken.ontimer(ring_liigu, 20)

# klaviatuurile reageerimine
aken.listen()
aken.onkeypress(liigu_vasakule, "Left")
aken.onkeypress(liigu_paremale, "Right")

ring_liigu()

aken.mainloop()