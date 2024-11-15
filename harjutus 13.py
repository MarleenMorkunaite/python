# 15.11.24 Marleen
# Harjutus 13

# Loo Pythoni Turtle-iga programm, mis palub kasutajal sisestada joonlaua pikkuse sentimeetrites kasutades numinput funktsiooni.

# Seejärel joonistab programm ekraanile joonlaua, märkides iga sentimeetri kriipsu ja numbri.
# Iga sentimeetri kriips peaks olema lühem ja iga viie sentimeetri tagant pikem, et eristada erinevaid mõõtmeid selgemalt.
# Numbrid kirjutatakse vastavate pikemate kriipsude juurde, märkides sentimeetrite arvu alates joonlaua algusest.


import turtle

screen = turtle.Screen()
t = turtle.Turtle()
t.speed(0)

# Küsi kasutajalt numbrilist sisendit
# nr = screen.numinput("Vanuse sisestamine", "Mis on sinu vanus?", default=20, minval=0, maxval=100)
# nr = 10
for i in range(nr+10):
    t.lt(90)
    t.fd(3)
    t.lt(180)
    t.fd(3)
    t.lt(90)
    t.fd(4)
t.goto(0,0)


for i in range(nr+1):
    t.lt(90)
    t.fd(5)
    t.write(i, font=("Arial", 10, "normal"))
    t.lt(180)
    t.fd(5)
    t.lt(90)
    t.fd(10*4)

turtle.done()



