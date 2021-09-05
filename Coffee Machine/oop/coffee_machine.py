from data import menu, profit, resources
class Coffee_machine():
	def __init__(self):
		pass
	
	def check_ing(self, need_ing):
		for thing in need_ing:
			if resources[thing] >= need_ing[thing]:
				return True
			else:
				print(f"We don't have enough {thing}. Try Contacting the Owner.")
				return False
	
	def cal_pay(self):
		total = int(input("How many quarters")) * 0.25
		total += int(input("How many dimes")) * 0.1
		total += int(input("How many nickles")) * 0.05
		total += int(input("How many pennies")) * 0.01
		return total
	
	
	def check_pay(self, payment, drink, choice):
		d_cost = drink["cost"]
		if payment >= d_cost:
			r_pay = round(payment - d_cost, 2)
			print("Here's your change {r_pay}.")
			return True
		else:
			print(f"Sorry! That's not enough Money for {choice}.")
			print(f"{choice} cost ${drink['cost']} but, you paid ${payment} only.")
			return False
	
	
	def choice(self):
		return input("What would you like to have? (Latte/Cappuccino/Espresso): ").lower()
	
	
	def owner_in(self, choice):
		if choice == "report":
			for item in resources:
				print(f"{item}		{resources[item]}")
			print(f"Profit		{profit}")
		else:
			drink = menu[choice]
			return drink
			

#	def off(self, choice):
#		if choice == "off":
#			return True
#	
#	def o_drink(self, choice):
#		if choice == "latte" or "cappuccino" or "espresso":
#			drink = menu[choice]
#			return drink