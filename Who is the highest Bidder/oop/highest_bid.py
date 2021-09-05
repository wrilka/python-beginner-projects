class High:
	def __init__(self):
		pass
	
	def name(self):
		name = input("What is your name?\n").lower()
		return name
	
	def amount(self):
		amount = int(input("What is the bidding amount?: "))
		return amount
	
	
	def highest_bidder(self, bids):
		high = 0
		name = ""
		for bidder in bids:
			bid = bids[bidder]
			if bid > high:
				high = bid
				name = bidder
		return print(f"The highest bidder is {name} with the bid of ${high}.")
	
	
	def other(self):
		other = input("Are there other Bidder 'y' or 'n': ").lower()
		return other
	