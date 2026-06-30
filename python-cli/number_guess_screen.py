import turtle
from random import randint

screen = turtle.Screen()
screen.setup(700, 450)
turtle.shape("turtle")
turtle.speed(0)


# Change background to new image
def set_background(image):
    screen.bgpic(image)


# Change turtle to new image
def set_sprite(image):
    screen.addshape(image)
    turtle.shape(image)


# Make turtle go to random position
def goto_random_pos():
    x = randint(-200, 200)
    y = randint(-150, 150)
    turtle.goto(x, y)


# stamp n copies of turtle image randomly on screen
def randomstamps(n):
    turtle.penup()
    for _ in range(n):
        goto_random_pos()
        turtle.stamp()
    # turtle.done()
    turtle.Screen().exitonclick()


set_background("space_bg.png")
# set_sprite("alien_ship.png")
randomstamps(10)
