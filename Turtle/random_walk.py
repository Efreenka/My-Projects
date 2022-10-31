from turtle import Turtle, Screen
import random
import turtle

# Změna barevného módu
turtle.colormode(255)

tommy = Turtle()
tommy.shape("turtle")


def random_color():
    r = random.randint(0, 255)
    g = random.randint(0, 255)
    b = random.randint(0, 255)
    random_color = (r, g, b)
    return random_color


rotation = [0, 90, 180, 270, 360]
speed = 1

for i in range(200):
    tommy.pencolor(random_color())

    # Tloušťka čáry
    if i <= 10:
        tommy.pensize(i)

    # Pohyb a náhodné otočení
    tommy.forward(30)
    tommy.left(random.choice(rotation))

    # Zvyšujeme rychlost
    tommy.speed(speed)
    speed += 1

my_screen = Screen()
my_screen.exitonclick()
