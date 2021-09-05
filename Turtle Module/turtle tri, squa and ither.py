from turtle import Turtle, Screen
import random


t = Turtle()
t.shape("turtle")
t.color("red")

colors = ["orange", "red", "blue", "black", "purple", "chocolate", "cyan3", "chartreuse1", "darkgoldenrod", "darkgoldenrod1"]

def run(no):
	angle = 360/no
	for _ in range(no):
		t.fd(100)
		t.right(angle)

for num in range(3, 11):
	t.color(random.choice(colors))
	run(num)

#for _ in range(3):
#	t.fd(100)
#	t.right(120)
#t.color("black")

#for _ in range(4):
#	t.fd(100)
#	t.right(90)
#t.color("purple")

#for _ in range(5):
#	t.fd(100)
#	t.right(72)
#t.color("chartreuse1")

#for _ in range(6):
#	t.fd(100)
#	t.right(60)
#t.color("chocolate")


#for _ in range(7):
#	t.fd(100)
#	t.right(51.4285714286)
#t.color("cyan2")

#for _ in range(8):
#	t.fd(100)
#	t.right(45)
#t.color("darkgoldenrod1")

#for _ in range(9):
#	t.fd(100)
#	t.right(40)
#t.color("deeppink1")

#for _ in range(10):
#	t.fd(100)
#	t.right(36)



my_screen = Screen()
my_screen.exitonclick()