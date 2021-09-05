import turtle as tim
from turtle import Screen
import random

t = tim.Turtle()
t.pensize(20)
tim.colormode(255)


def random_color():
	r = random.randint(0, 255)
	g = random.randint(0, 255)
	b = random.randint(0, 255)
	rgb = (r, g, b)
	return rgb


direction = [0, 90, 180, 270]
t.speed(0)

for _ in range(250):
	t.color(random_color())
	t.fd(50)
	t.setheading(random.choice(direction))

screen = Screen()
screen.exitonclick()