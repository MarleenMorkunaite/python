# 18.10.24 Marleen
# Ülesanne 6

import turtle
import math 
kordaja = 10
a = 53
h = 4.4
x = abs(h / math.tan(a))
c = math.sqrt(h**2 + x** 2)

print(x)


turtle.fd(x*kordaja)
turtle.left(90)
turtle.fd(10*kordaja)
turtle.left(180-66)
turtle.fd(14*kordaja)

turtle.done()
