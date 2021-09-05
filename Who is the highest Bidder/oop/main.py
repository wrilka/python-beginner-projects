from highest_bid import High
from bidder import Bidder

h = High()

bid ={}

again = True
while again:
	name = h.name()
	amount = h.amount()
	bid[name] = amount
	
	other = h.other()
	if other == "n":
		h.highest_bidder(bid)
		again = False