import turtle

import math

import time



t = turtle.Turtle()





def fnA(x, y):

    t.penup()

    t.goto(x, y)

    t.pendown()

    t.setheading(0)

    t.pensize(2)

    t.speed(10)





def fnB(r, color):

    x_point = 0

    y_pont = -r

    fnA(x_point, y_pont)

    t.pencolor(color)

    t.fillcolor(color)

    t.begin_fill()

    t.circle(r)

    t.end_fill()





def fnC(r, color):

    fnA(0, 0)

    t.pencolor(color)

    t.setheading(162)

    t.forward(r)

    t.setheading(0)

    t.fillcolor(color)

    t.begin_fill()

    for i in range(5):

        t.forward(math.cos(math.radians(18)) * 2 * r)  # 2cos18°*r

        t.right(144)

    t.end_fill()

    t.hideturtle()





if __name__ == '__main__':

    time.sleep(5)

    fnB(288, 'crimson')

    fnB(234, 'snow')

    fnB(174, 'crimson')

    fnB(114, 'blue')

    fnC(114, 'snow')

    turtle.done()
