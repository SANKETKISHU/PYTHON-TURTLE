#import turtle
import turtle

# set screen
Screen = turtle.Turtle()

# decide colors
cir= ['red','green','blue','yellow','purple']

# decide pensize
turtle.pensize(4)

# Draw star pattern
turtle.penup()
turtle.setpos(-90,30)
turtle.pendown()
for i in range(5):
	turtle.pencolor(cir[i])
	turtle.forward(200)
	turtle.right(144)

turtle.penup()
turtle.setpos(80,-140)
turtle.pendown()

# choose pen color
turtle.pencolor("Black")
turtle.done()
