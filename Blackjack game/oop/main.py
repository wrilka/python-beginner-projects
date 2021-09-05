from blackjack import Blackjack

b = Blackjack()

deal_card = b.deal_card()

u_card = []
c_card = []
b.draw(u_card, c_card)
game_end = False
while not game_end:
	u_score = b.cal_score(u_card)
	c_score = b.cal_score(c_card)
	
	b.show_card(u_card, c_card)
	game_end = b.blackjack(u_score, c_score)
	if game_end == True:
		break
	another = b.ask()
	game_end = b.an_card(another, u_card)

while c_score != 0 and c_score < 17:
	c_card.append(deal_card)
	c_score = b.cal_score(c_card)
print(f"\nYour Cards are {u_card}. Score is {u_score}.")
print(f"Computer cards are {c_card}. Score is {c_score}.\n")
print(b.compare(u_score, c_score))