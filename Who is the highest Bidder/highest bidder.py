
def finding_highest_bidder(bids_amount):
	highest_bid = 0
	winner = ""
	for bidder in bids_amount:
		bid = bids_amount[bidder]
		if bid > highest_bid:
			highest_bid = bid
			winner = bidder
			
	print(f"The winner is {winner} and bid amount is ${highest_bid}")


bids = {}

bidding_finished = False
while not bidding_finished:
	name = input("What is the name of bidder?: ")
	amount = int(input("What is your bidding price?: $"))
	bids[name] = amount

	again = input("Are there any other bidders. Type 'yes' or 'no'").lower()
	if again == "yes":
		pass
	elif again == "no":
	  bidding_finished = True
	  finding_highest_bidder(bids)
		