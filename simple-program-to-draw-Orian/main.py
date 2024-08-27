"""_summary_
            simple program to draw Orian (https://en.wikipedia.org/wiki/Orion_(constellation))
"""
import turtle as t, time

# little notice the starting point is Alnilam star 
xSTARTINGPOINT = 0 
ySTARTINGPOINT = 0

xMEISSA = 80
yMEISSA = 180

xMINTAKA = 40
yMINTAKA = 20

xALNITAK = -40
yALNITAK = -20

xBETELGEUSE = -70
yBETELGEUSE = 200

xRIGEL = 120
yRIGEL = -140

xSAIPH = -90
ySAIPH = -180

t.goto(xMINTAKA, yMINTAKA)
t.dot()
t.write("Minataka")

t.goto(xMEISSA, yMEISSA)
t.dot()
t.write("Meissa")

t.penup()
t.goto(xSTARTINGPOINT, ySTARTINGPOINT)
t.pendown()
t.dot()
t.write("Alnilam")

t.goto(xALNITAK, yALNITAK)
t.dot()
t.write("Alnitak")

t.goto(xBETELGEUSE, yBETELGEUSE)
t.dot()
t.write("Betelgeuse")

t.penup()
t.goto(xMINTAKA, yMINTAKA)
t.pendown()

t.goto(xRIGEL, yRIGEL)
t.dot()
t.write("Rigle")

t.penup()
t.goto(xALNITAK, yALNITAK)
t.pendown()

t.goto(xSAIPH, ySAIPH)
t.dot()
t.write("Saiph")

time.sleep(2)
