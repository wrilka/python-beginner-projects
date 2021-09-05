words = ["Prachanda", "Bitisha", "Srijana", "Dilip"]

import random

random_word = random.choice(words)

user_word = input("Guess a Word\n").lower()

for word in random_word:
	if user_word == word:
		print("Right")
	else:
		print("Wrong")