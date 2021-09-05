import random
again = True

random_cards= [11, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]

start = input("Do you want to play this game 'y' or 'n'").lower()
user_cards = []
comp_cards = []
if start == "y":
	comp_card1 = random.choice(random_cards)
	comp_cards += str(comp_card1)
	comp_card2 = random.choice(random_cards)
	comp_cards += str(comp_card2)
	#one_comp_card = comp_cards[0]
	print(f"Computer first card is '{comp_card1}' and second will not be shown")
	user_card1 = random.choice(random_cards)
	user_cards += str(user_card1)
	user_card2 = random.choice(random_cards)
	user_cards += str(user_card2)
	print(f"Your cards are '{user_card1}' and '{user_card2}'")
	add_user = user_card1 + user_card2
	add_comp = comp_card1 + comp_card2
	while again == True:
		if add_user == 21 and add_comp == 21:
			print("You Lose")
		if add_user == 21:
			print("You Win")
		elif add_comp == 21:
			print("You Lose")
		if add_user != 21 and add_comp != 21:
			if add_user > 21:
				if 11 in user_cards:
					print("I don't know")
				else:
					print("You Lose")
			else:
				another_card = input("Do you want another card 'y' or 'n'")
				if another_card == "y":
					user_card3 = random.choice(random_cards)
					user_cards += str(user_card3)
					add_user = user_card1 + user_card2 + user_card3
				else:
					again = False
else:
	print("You Lose")