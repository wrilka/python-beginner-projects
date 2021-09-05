menu = {
    "espresso": {
        "ingredients": {
            "water": 50,
            "milk": 0,
            "coffee": 18
        },
        "cost": 1.5,
    },
    "latte": {
        "ingredients": {
            "water": 200,
            "milk": 150,
            "coffee": 24,
        },
        "cost": 2.5,
    },
    "cappuccino": {
        "ingredients": {
            "water": 250,
            "milk": 100,
            "coffee": 24,
        },
        "cost": 3.0,
    }
}

profit = 0
resources = {
    "water": 500,
    "milk": 400,
    "coffee": 250,
}

def add_resources():
	for things in resources:
		resources[things] += 2000

def checking_ingredients(needed_ingredients):
	for things in needed_ingredients:
		if needed_ingredients[things] * qun > resources[things]:
			print(f"You don't have enough {things} for {need}")
			return False
		else:
			return True
	
def checking_payment():
	total = int(input("How many Quarters?: ")) * 0.25
	total += int(input("How many Dimes?: ")) * 0.1
	total += int(input("How many Nickles?: ")) * 0.05
	total += int(input("How many Pennies?: ")) * 0.01
	return total

def calculating_payment(payment, needed_cost):
	needed_cost *= qun
	if payment >= needed_cost:
		return_money = round(payment - needed_cost, 2)
		print(f"Here's the change ${return_money}")
		global profit
		profit += needed_cost
		return True
	else:
		print(f"You don't have enough money for {need} which costs ${user_drink['cost']}")
		return False

def reduce_resources(drink, ingredients):
	for things in ingredients:
		resources[things] -= ingredients[things] * qun
	print(f"Here is your {need} which costs ${user_drink['cost'] * qun}")





off = False
while off != True:
	need = input("What would you like to have? (latte/espresso/cappuccino): ").lower()
	if need == "report":
		for x,y in resources.items():
			print(f"{x}:\t{y}")
		print(f"money:\t{profit}")
	elif need == "add":
		add_resources()
	elif need == "off":
		off = True
	else:
		user_drink = menu[need]
		qun = int(input(f"How many cup of {need} do you want?: "))
		if checking_ingredients(user_drink["ingredients"]):
			print("Insert your coins")
			payment = checking_payment()
			if calculating_payment(payment, user_drink["cost"]):
				reduce_resources(need, user_drink["ingredients"])