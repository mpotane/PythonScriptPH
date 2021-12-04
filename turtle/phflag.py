from turtle import *


def blue():
    flag.penup()
    flag.goto(-400, 0)
    flag.pendown()

    # Blue rectangle
    flag.color('blue')
    flag.begin_fill()
    flag.forward(800)
    flag.left(90)
    flag.forward(250)
    flag.left(90)
    flag.forward(800)
    flag.end_fill()


def red():
    flag.penup()
    flag.goto(-400, -250)
    flag.pendown()

    # Red rectangle
    flag.color('firebrick')
    flag.begin_fill()
    flag.forward(800)
    flag.left(90)
    flag.forward(250)
    flag.left(90)
    flag.forward(800)
    flag.end_fill()


def white():
    flag.penup()
    flag.goto(-400, 250)
    flag.pendown()

    # Triangle
    flag.color('white')
    flag.begin_fill()
    flag.forward(500)
    flag.left(130)
    flag.forward(390)
    flag.end_fill()


def star():
    flag.color('yellow')
    flag.left(36)
    flag.begin_fill()
    for _ in range(5):
        flag.forward(30)
        flag.left(144)
    flag.end_fill()


def sun():
    flag.penup()
    flag.goto(-290, -50)
    flag.pendown()

    # Drawing the sun
    flag.color('orange', 'yellow')
    flag.pensize(5)
    flag.begin_fill()
    flag.circle(50)
    flag.end_fill()
    # Drawing rays
    for _ in range(8):
        flag.rt(92)
        flag.fd(40)
        flag.bk(40)
        flag.lt(92)
        flag.circle(50, 45)


if __name__ == '__main__':
    flag = Turtle()
    s = Screen()
    s.title('Welcome to Python PH!')
    flag.speed(0)
    s.setup(800, 500)
    blue()
    flag.left(180)
    red()
    flag.left(90)
    white()
    flag.penup()
    flag.goto(-375, 185)
    flag.pendown()
    star()
    flag.penup()
    flag.goto(-368, -210)
    flag.pendown()
    star()
    flag.penup()
    flag.goto(-120, 0)
    flag.pendown()
    star()
    flag.left(214)
    sun()
    flag.hideturtle()
    done()
