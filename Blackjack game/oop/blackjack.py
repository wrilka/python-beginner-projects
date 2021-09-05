class Blackjack:
	def __init__(self):
		pass
	
	def deal_card(self):
		import random
		cards = [11, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]
		card = random.choice(cards)
		return card
	
	def draw(self, u_card, c_card):
		for _ in range(2):
			u_card.append(self.deal_card())
			c_card.append(self.deal_card())
	
	def cal_score(self, card):
		if sum(card) == 21 and len(card) == 2:
			return 0
		if 11 in card and sum(card) > 21:
			card.remove(11)
			card.append(1)
		return sum(card)	
	
	
	def show_card(self, u_card, c_card):
		print(f"\nComputer first card is {c_card[0]}.")
		print(f"User Cards are {u_card} and score is {sum(u_card)}.")
	
	def blackjack(self, u_score, c_score):
		if u_score == 0 or c_score == 0:
			return True
	
	def ask(self):
		another = input("Do you want another card. 'y' or 'n': ").lower()
		return another
	
	def an_card(self, another, u_card):
		if another == "y":
			u_card.append(self.deal_card())
		else:
			return True

	def compare(self, user_score, computer_score):
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