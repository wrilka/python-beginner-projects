MENU = {
    "espresso": {
        "ingredients": {
            "water": 50,
            "coffee": 18,
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
    "water": 300,
    "milk": 200,
    "coffee": 100,
}

def add_resources(all_resources):
	for thing in all_resources:
		all_resources[thing] += 1000

def check_ingredients(needed_ing):
	for thing in needed_ing:
		if needed_ing[thing] * num > resources[thing]:
			print(f"Sorry! We don't have enough {thing}")
			return False
		else:
			return True

def calculate_coin():
	total = int(input("How many quarters")) * 0.25
	total += int(input("How many dimes")) * 0.1
	total += int(input("How many nickles")) * 0.05
	total += int(input("How many pennies")) * 0.01
	return total

def check_transaction(payment, drink_cost):
	drink_cost = drink_cost * num
	if payment >= drink_cost:
		return_amount = round(payment - drink_cost, 2)
		global profit
		profit += drink_cost
		print(f"Here's your change ${return_amount}")
		return True
	else:
		print(f"Not enough money for a {choice} which cost ${drink_cost}. Money Refunded ${round(payment, 2)}")
		return False

def your_coffee(coffee_ingredients):
	for item in coffee_ingredients:
		resources[item] -= coffee_ingredients[item] * num
	print(f"Here is your {choice} which cost ${drink['cost'] * num}. ENJOY")

on = True
while on:
	choice = input("What would you like to have sir/mam? (espresso/latte/cappuccino): ").lower()
	if choice == "report":
		print(f"Water: {resources['water']}ml")
		print(f"Milk: {resources['milk']}ml")
		print(f"Coffee: {resources['coffee']}g")
		print(f"Money: ${profit}")
	elif choice == "add":
		add_resources(resources)
	elif choice == "off":
		on = False
	else:
		num = int(input("How many cups of {choice} Do you Want?: "))
		drink = MENU[choice]
		if check_ingredients(drink["ingredients"]):
			print("Insert a coin")
			payment = calculate_coin()
			if check_transaction(payment, drink["cost"]):
				your_coffee(drink["ingredients"])