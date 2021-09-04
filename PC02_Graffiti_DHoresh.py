#!/usr/bin/env python
# coding: utf-8

'''
Turtle starter code
ATLS 1300
Author: Dr. Z
Author: Dover Horesh
August 31, 2021
'''

import turtle #import the library of commands that you'd like to use

turtle.colormode(255)

# Create a panel to draw on. 
panel = turtle.Screen()
w = 750 # width of panel
h = 750 # height of panel
panel.setup(width=w, height=h) #600 x 600 is a decent size to work on. 
#You can experiment by making it the size of your screen or super tiny!

# Create a colorful background and add Bezos image to it
image = "Bezos.gif"
turtle.Screen().bgcolor(129,205,80)
panel.bgpic(image)

#=======Add your code here======

t=turtle
t.pen(pencolor="red", fillcolor="red", pensize=4, speed=10)
t.title ("Clown King Bezos")



t.up()
t.goto(-85,140)
t.down()

#filling in the clown hair on the left
t.fillcolor(176, 32, 39)

t.begin_fill()
t.circle(30)
t.end_fill()

t.begin_fill()
t.goto(-110,150)
t.circle(20)
t.end_fill()


t.begin_fill()
t.goto(-130,160)
t.circle(13)
t.end_fill()



#make Bezos a crown

t.up()
t.goto(-75,210)
t.down()

t.pen(pencolor="yellow", fillcolor="yellow", pensize=5, speed=10)
t.fillcolor(255,193,0)

t.begin_fill()
t.left(10)
t.forward(70)

#make crown spikes
t.left(70)
t.forward(90)
t.left(160)
t.forward(40)

t.right(130)
t.forward(40)
t.left(150)
t.forward(40)

t.right(150)
t.forward(40)
t.left(150)
t.forward(40)

t.right(150)
t.forward(40)
t.left(150)
t.forward(40)

t.right(120)
t.forward(40)
t.left(150)
t.goto(-75,210)
#finish crown
t.end_fill()



#make Clown Hair right side
t.pen(pencolor="red", fillcolor="red", pensize=4, speed=10)
t.fillcolor(176, 32, 39)

t.up()
t.goto(100,190)
t.down() 
t.begin_fill()
t.circle(10)
t.end_fill()

t.up()
t.goto(75,175)
t.down()
t.begin_fill()
t.circle(20)
t.end_fill()

t.up()
t.goto(40,190)
t.down()
t.begin_fill()
t.forward(40)
t.left(100)
t.forward(40)
t.left(90)
t.forward(15)
t.goto(40,190)

t.end_fill()

t.right(180)
t.forward(20)
t.begin_fill()
t.circle(25,360)
t.end_fill()

t.up()
t.goto(20,80)
t.down()

t.begin_fill()
t.circle(10)
t.end_fill()
 #end hair

t.up()
t.goto(0,0)
t.pen(pencolor="black", fillcolor="black", pensize=4, speed=10)

t.goto(15,65)
t.down()
t.left(20)
t.circle(50,90)

t.up()
t.goto(15,65)
t.down()
t.right(180)
t.circle(-50,90)


t.pen(pencolor="silver", fillcolor="blue", pensize=4, speed=10)


t.up()
t.goto(-25,245)
t.down()

t.circle(10)



#=======Clean up code (do not change)======
# this code ensures that your script runs correctly each time.
turtle.done()
