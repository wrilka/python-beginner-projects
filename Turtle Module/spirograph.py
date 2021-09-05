import turtle as tim
from turtle import Screen
import random

t = tim.Turtle()
t.speed(0)
tim.colormode(255)


def random_color():
	r = random.randint(0, 255)
	g = random.randint(0, 255)
	b = random.randint(0, 255)
	rgb = (r, g, b)
	return rgb

def spirograph(gap):
	for _ in range(int(360/gap)):
		t.color(random_color())
		t.circle(100)
		t.setheading(t.heading() + gap)

#change size or gap here
spirograph(5)


screen = Screen()
screen.exitonclick()