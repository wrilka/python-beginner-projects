class Followers:
	def __init__(self):
		pass
	
	def random_ac(self, random_ac):
		name = random_ac["name"]
		description = random_ac["description"]
		country = random_ac["country"]
		return f"{name}, a {description}, from {country}"
	
	
	def u_ans(self):
		ans = input("Who has more follower 'a' or 'b': ").lower()
		return ans
	
	def check_answer(self, ans, a_fol, b_fol):
		if a_fol > b_fol:
			if ans == "a":
				scores = print("\nThat's Right!")
				loop = False
				return scores, loop
			else:
				scores = print(f"\nYou are Wrong!")
				loop = True
				return scores, loop
		if b_fol > a_fol:
			if ans == "b":
				scores = print(f"\nThat's Right!")
				loop = False
				return scores, loop 
			else:
				scores = print(f"\nYou are Wrong!")
				loop = True
				return scores, loop
				