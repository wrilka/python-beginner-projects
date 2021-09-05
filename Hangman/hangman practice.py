import random

stages = ['''
  +---+
  |   |
  O   |
 /|\  |
 / \  |
      |
=========
''', '''
  +---+
  |   |
  O   |
 /|\  |
 /    |
      |
=========
''', '''
  +---+
  |   |
  O   |
 /|\  |
      |
      |
=========
''', '''
  +---+
  |   |
  O   |
 /|   |
      |
      |
=========''', '''
  +---+
  |   |
  O   |
  |   |
      |
      |
=========
''', '''
  +---+
  |   |
  O   |
      |
      |
      |
=========
''', '''
  +---+
  |   |
      |
      |
      |
      |
=========
''']

def word(guess, r_word):
	for s_char in range(len(r_word)):
		letter = r_word[s_char]
		if guess == letter:
			emp[s_char] = guess
	return emp

words_r = ["cheeey", "pumpkin", "carrot", "cucumber"]

r_word = random.choice(words_r)

emp = []
for li in range(len(r_word)):
	emp += "_"
lives = 6
print("You only got 6 Lives")
game_end = False
while not game_end:
	guess = input("Guess a letter: ")
	if guess in emp:
		print("You have already guessed that one")
	
	print(word(guess, r_word))

	if guess not in r_word:
		lives -= 1
		print(f"You are wrong. You lost a live and you have {lives} remaining")
	
	if "_" not in emp:
		game_end = True
		print("You Won! You have managed to guess all right")
	if lives == 0:
		game_end = True
		print("You are out of guess. You Lost!")
	print(stages[lives])