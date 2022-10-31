from turtle import Turtle, Screen
import random
import turtle

# Změna barevného módu
turtle.colormode(255)

# Generování a základní nastavení objektu
tommy = Turtle()
tommy.shape("turtle")
tommy.speed(20)


# Funkce na generování barvy
def random_color():
    r = random.randint(0, 255)
    g = random.randint(0, 255)
    b = random.randint(0, 255)
    random_color = (r, g, b)
    return random_color


def spirograph(number):
    for i in range(int(360/number)):
        tommy.pencolor(random_color())
        tommy.circle(80)
        tommy.left(number)


spirograph(1)

my_screen = Screen()
my_screen.exitonclick()
