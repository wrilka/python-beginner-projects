import random

def deal_card():
	cards= [11, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]
	card = random.choice(cards)
	return card

def calculator_score(uc_cards):
	if sum(uc_cards) == 21 and len(uc_cards) == 2:
		return 0
		
	if 11 in uc_cards and sum(uc_cards) > 21:
		uc_cards.remove(11)
		uc_cards.append(1)
		
	return sum(uc_cards)

def compare(user_score, computer_score):
	if user_score == computer_score:
		return "It's a Draw!"
	elif computer_score == 0:
		return "You Lose! 'Computer has BlackJack'"
	elif user_score == 0:
		return "You win! 'You have BlackJack'"
	elif user_score > 21:
		return "You Lose! 'You went over 21"
	elif computer_score > 21:
		return "You win! 'Computer went over 21'"
	elif user_score > computer_score:
		return "You Win! 'You have more score'"
	elif computer_score > user_score:
		return "You Lose! 'Computer have more Score'"

user_card= []
computer_card = []
game_over = False

for _ in range(2):
	user_card.append(deal_card())
	computer_card.append(deal_card())

while not game_over:
	user_score= calculator_score(user_card)
	computer_score= calculator_score(computer_card)
	
	print(f"Your cards are {user_card} and Your Score is {user_score}")
	print(f"Computer first card is {computer_card[0]}")
	
	if user_score == 0 and computer_score == 0 and user_score > 21:
		game_over = True
	else:
		another_card = input("Do you want another card or Pass. Type 'y' for another and 'n' for Pass: ").lower()
		if another_card == "y":
			user_card.append(deal_card())
		else:
			game_over = True

while computer_score != 0 and computer_score < 17:
	computer_card.append(deal_card())
	computer_score = calculator_score(computer_card)

print(f"Computer cards are {computer_card} and Final Score is: '{computer_score}'")
print(f"Your Cards are {user_card} and Final Score is: '{user_score}'")
print(compare(user_score, computer_score)).