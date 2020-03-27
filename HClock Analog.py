#!/usr/bin/env python3
# Analog clock for Holoclock
# Created by BitMan64

import turtle
import time
wn = turtle.Screen()
wn.bgcolor("black")
wn.setup(width=800,height=480)
wn.title("HClock Analog")
wn.tracer(0)

pen = turtle.Turtle()
pen.hideturtle()
pen.speed(0)
pen.pensize(4)

def Clock_Face(h,m,s,pen):
    pen.up()
    pen.goto(0,200)
    pen.setheading(180)
    pen.color("green")
    pen.pendown()
    ##pen.circle(200)


    pen.penup()
    pen.goto(0,0)
    pen.setheading(180)


    for _ in range(12):
        pen.fd(190)
        pen.pendown()
        pen.fd(20)
        pen.penup()
        pen.goto(0,0)
        pen.rt(30)

    for _ in range(60):
        pen.fd(205)
        pen.pendown()
        pen.fd(5)
        pen.penup()
        pen.goto(0,0)
        pen.rt(6)

    ##Hour Hand
    pen.pensize(4)
    pen.penup()
    pen.goto(0,0)
    pen.color("green")
    pen.setheading(90)
    angle = (h / 12) * -360
    pen.rt(angle)
    pen.pendown()
    pen.fd(90)

    ##Minute Hand
    pen.pensize(4)
    pen.penup()
    pen.goto(0,0)
    pen.color("green")
    pen.setheading(90)
    angle = (m / 60) * -360
    pen.rt(angle)
    pen.pendown()
    pen.fd(130)

    ##Second Hand
    pen.pensize(3)
    pen.penup()
    pen.goto(0,0)
    pen.color("red")
    pen.setheading(90)
    angle = (s / 60) * -360
    pen.rt(angle)
    pen.pendown()
    pen.fd(180)

while True:
    ##Get the current system time
    h = int(time.strftime("%I"))
    m = int(time.strftime("%M"))
    s = int(time.strftime("%s"))
    Clock_Face(h,m,s,pen)

    wn.update()
    time.sleep(0.5)
    
    pen.clear()




wn.mainloop()
