import random
def deck_card():
	cards = [11, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]
	card = random.choice(cards)
	return card

def calculate_score(cards):
	if sum(cards) == 21 and len(cards) == 2:
		return 0
	if sum(cards) > 21 and 11 in cards:
		cards.remove(11)
		cards.append(1)
	return sum(cards)

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

end_game = False
user_cards = []
computer_cards = []

for _ in range(2):
	user_cards.append(deck_card())
	computer_cards.append(deck_card())

while not end_game:
	user_score = calculate_score(user_cards)
	computer_score = calculate_score(computer_cards)
	
	print(f"Your Cards are {user_cards} and score is {user_score}")
	print(f"Computer Card is {computer_cards[0]}")
	
	if user_score == 21 and user_score == 0 and computer_score == 0:
		end_game = True
	else:
		another = input("Do you want another card? 'y' or 'n'")
		if another == "y":
			user_cards.append(deck_card())
		else:
			end_game = True

while computer_score != 0 and computer_score < 17:
	computer_cards.append(deck_card())
	computer_score = calculate_score(computer_cards)

print(f"Computer cards are {computer_cards} and Final Score is: '{computer_score}'")
print(f"Your Cards are {user_cards} and Final Score is: '{user_score}'")

print(compare(user_score, computer_score))