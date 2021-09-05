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

def check_ingredients(need_ingre):
	for thing in need_ingre:
		if resources[thing] >= need_ingre[thing]:
			return True
		else:
			print("Sorry! we don't have enough for a {choice}.")
			return False


def calculate_coin():
	total = int(input("How many quarters: ")) * 0.25
	total += int(input("How many dimes: ")) * 0.1
	total += int(input("How many nickles: ")) * 0.05
	total += int(input("How many pennies: ")) * 0.01
	return total


def check_pay(payment):
	d_cost = drink["cost"]
	if payment >= d_cost:
		global profit
		profit += d_cost
		ret_am = round(payment - d_cost, 2)
		print(f"Here's a change {ret_am}")
		return True
	else:
		print(f"Sorry! That's not enough money.")
		print(f"Here's a refund. {choice} costs {d_cost}$ But, you paid {payment}$.")
		return False


def give_drink():
	d_ing = drink["ingredients"]
	for item in d_ing:
		resources[item] - d_ing[item]
	print(f"Here is your {choice} which cost ${drink['cost']}. ENJOY")



turn_off = False
while turn_off == False:
	choice = input("What woud you like to have? (espresso/latte/cappuccino: ").lower()
	if choice == "report":
		print(f"Water		{resources['water']}")
		print(f"Milk		{resources['milk']}")
		print(f"Coffee 		{resources['coffee']}")
		print(f"Profit		{profit}")
	elif choice == "off":
		turn_off = True
	else:
		drink = MENU[choice]
		if check_ingredients(drink["ingredients"]):
			payment = calculate_coin()
			if check_pay(payment):
				give_drink()