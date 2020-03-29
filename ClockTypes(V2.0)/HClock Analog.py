#!/usr/bin/env python3
# Analog clock for my Holoclock project for the
# Instructables 2020 Clock Contest at
# https://www.instructables.com/contest/clocks2020/
# Created by BitMan64

import turtle
import time

wn = turtle.Screen()
wn.bgcolor("black")
wn.setup(width=800, height=480)
wn.title("Analog Clock")
wn.tracer(0)

pen = turtle.Turtle()
pen.hideturtle()
pen.speed(0)
pen.pensize(4)

def outerRimLines(pen, rng, start, length):
    # Draw markers at the rim of the clock
    pen.up()
    pen.goto(0, 0)
    pen.setheading(180)
    rotation = 360 / rng
    for i in range(rng):
        pen.penup()
        pen.fd(start)
        pen.pendown()
        pen.fd(length)
        pen.penup()
        pen.goto(0, 0)
        pen.rt(rotation)
    pen.up()

def clockHand(pen, size, angle, linelen):
    # Draw a clock hand
    pen.penup()
    pen.goto(0, 0)
    pen.setheading(90)
    pen.pensize(size)
    pen.pendown()
    pen.rt(angle)
    pen.fd(linelen)
    pen.penup()

def Clock_Face(h, m, s, pen):
    pen.up()
    pen.goto(0, 200)
    pen.down()
    
    # Hour lines
    pen.color("green")
    outerRimLines(pen, 12, 190, 20)
    
    # Minute lines
    outerRimLines(pen, 60, 205, 5)

    ##Hour Hand
    pen.color("green")
    angle = (m / 60) * -360
    clockHand(pen, 4, angle, 90)

    ##Minute Hand
    pen.color("green")
    angle = (h / 12) * -360
    clockHand(pen, 4, angle, 130)

    ##Second Hand
    pen.color("red")
    angle = (s / 60) * -360
    clockHand(pen, 3, angle, 180)

def run():
    while True:
        # Get the current system time
        h = int(time.strftime("%I"))
        m = int(time.strftime("%M"))
        s = int(time.strftime("%s"))
        Clock_Face(h, m, s, pen)
        
        wn.update()
        time.sleep(0.5)
        
        pen.clear()

if __name__ == '__main__':
    run()
