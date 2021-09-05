from all_data import data
from follower import Followers
import random

f = Followers()
score = 0
r_ac_b = random.choice(data)
game_end = False
while game_end == False:
	r_ac_a = r_ac_b
	r_ac_b = random.choice(data)
	if r_ac_a == r_ac_b:
		r_ac_b = random.choice(data)
	
	print(f"Compare A: {f.random_ac(r_ac_a)}")
	print("VS")
	print(f"Against B: {f.random_ac(r_ac_b)}")
	
	ans = f.u_ans()
	
	a_fol = r_ac_a["follower_count"]
	b_fol = r_ac_b["follower_count"]
	
	
	scores, loop = f.check_answer(ans, a_fol, b_fol)
	
	scores
	score += 1
	game_end = loop
	if game_end == False:
		print(f"Your initial Score is {score}.\n\n")
	elif game_end == True:
		print(f"Your Final Score is {score}.")