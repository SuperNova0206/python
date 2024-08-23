"""_summary_
            making a simple program for drawing a triangle using turtle and time modules

"""
import turtle as t, time 
CM = 37.80 # this is the value of 1 cm converted into pixel 
time.sleep(3)
t.showturtle()
# horizontal line 
for i in range(6) : 
    if i == 5 : 
        t.forward(CM)
        break
    t.forward(CM)
    t.dot() 
    t.write(i + 1)
t.penup()
t.goto(0, 0)
t.pendown()
t.setheading(180)
for i in range(6) : 
    if i == 5 : 
        t.forward(CM)
        break
    t.forward(CM)
    t.dot() 
    t.write(f"-{i+1}", align="center")
# making vertical line
t.penup()
t.goto(0, 0)
t.setheading(90)
t.pendown()
for i in range(6) : 
    if i == 5 : 
        t.forward(CM)
        break
    t.forward(CM)
    t.dot() 
    t.write(i + 1, align="right")
t.penup()
t.goto(0, 0)
t.setheading(270)
t.pendown()
for i in range(6) : 
    if i == 5 : 
        t.forward(CM)
        break
    t.forward(CM)
    t.dot() 
    t.write(f"-{i+1}", align="right")

# drawing the triangle
X = CM * 5
Y = CM * 5
t.penup()
t.goto(X, Y)
t.pendown()
t.setheading(280)
t.begin_fill()
t.forward(CM*5)
t.setheading(200)
t.forward(CM*5)
t.goto(X, Y)
time.sleep(3)