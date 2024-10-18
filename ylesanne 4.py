# 16.10.24
#ülesanne 04


"""
import turtle
# 5. Ringi pindala ja Turtle
try: 
    r = int(input("Lisa ringi raadius: "))
    Pi = 3.14
    s = pi*r**2
    P = 2*pi*r
    print(f"Ringi pindala on {s: .2f} ja ümbermõõt on {p:.2f} ")
    turtle.circle(r, 360)
except:
    print("Tegid sisestamisel vea!")
"""



"""
# 4. Kingituste pakkimine
try:
    Kingitused = int(input("Lisa kinkide arv: "))
    maht = 5
    pakid = kingitused // maht
    yle = kingitused % maht
    print(f"Saad teha {pakid} täis kinkekasti. Üle jääb {yle} kingitust.")
except: 
    print("Tegid sisstamisel vea!")
"""


"""
# 3. Faili allalaadimine
try:
    Failisuurus = int(input("Sisesta faili suurus (MB): "))
    downKiirus = int(input("Sisesta allalaadimis kiirus(MB/s): "))
    aeg = Failisuurus / downKiirus
except:
    print(f"Allalaadimiseks kulub {aeg:0.2f} sekundit")
"""


"""
# 2. Raamatute allahindlus
ale = 0.2
kogus = 3
hind = 12.53
summa = hind - (hind * ale) *kogus
print(f"{kogus} raamatu hind soodustusega on {summa: 0.2F}€")
"""

"""
# 1. Aia pikkus
a = int(input("Sisesta külg 1: "))
b = int(input("Sisesta külg 2: "))
p = 2 *(a + b)
print(f"Aia kogupikkus on 18 meetrit.")
"""

turtle.done()