from random_number import fruits
from hangman import Hang
import random

hangman = Hang()


random_word = random.choice(fruits)
print(random_word)

bracket = hangman.show_bracket(random_word)


live = 6
print("You got 6 lives")
game_end = False
while game_end == False:
	user_word = input("Guess a Word: ").lower()
	if user_word in bracket:
		print("you have already fuesses that one")
	
	print(hangman.check_word(user_word, random_word))	
	if not user_word in random_word:
		live -= 1
		print("That's wrong")
		print(f"You lost a live and you got {live} remaining")
	if live == 0:
		game_end = True
		print("You have run out of guess")
	if "_" not in bracket:
		print("You won!")
		game_end = True