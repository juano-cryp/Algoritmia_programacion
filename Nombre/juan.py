import turtle
import random
import colorsys

def random_rgb():
    return (random.random(), random.random(), random.random())


t = turtle.Turtle()
turtle.bgcolor("black") 
t.speed(0)
t.color("black")
h = 0

for i in range(360):
    c = colorsys.hsv_to_rgb(h, 1, 1)
    t.pencolor(c)
    t.forward(i)
    t.right(59)
    h += 1 / 360  
t.penup()
t.goto(-100, 60)  
t.pendown()


t.pensize(15) #Tamaño de las letras 

# Letra J
t.color(random_rgb())
t.left(180)
t.forward(100)
t.left(180)
t.forward(50)
t.right(90)
t.forward(80)
t.right(90)
t.forward(50)

# letra (U)
t.penup()
t.pendown()  

# Letra U
t.color(random_rgb())
t.penup()
t.left(180)
t.forward(50)
t.left(90)
t.forward(80)
t.right(90)
t.forward(70)
t.pendown()
t.right(90)
t.forward(80)
t.left(90)
t.forward(50)
t.left(90)
t.forward(80)

#  letra (A)
t.penup()
t.pendown()

# Letra A
t.color(random_rgb())
t.penup()
t.left(180)
t.forward(80)
t.left(90)
t.forward(20)
t.pendown()
t.left(90)
t.forward(80)
t.right(90)
t.forward(40)
t.right(90)
t.forward(40)
t.right(90)
t.forward(40)
t.left(180)
t.forward(40)
t.right(90)
t.forward(40)

# letra (N)
t.penup() 
t.pendown()

# Letra N
t.color(random_rgb())
t.penup()
t.left(90)
t.forward(20)
t.pendown()
t.left(90)
t.forward(80)
t.right(150)
t.forward(90)
t.left(150)
t.forward(80)

t.hideturtle()


turtle.done()
