from data import menu, profit, resources
from coffee_machine import Coffee_machine

c = Coffee_machine()


choice = c.choice()
drink = c.owner_in(choice)
if c.check_ing(drink["ingredients"]):
	payment = c.cal_pay()
	if c.check_pay(payment, drink, choice):
		print("hello")