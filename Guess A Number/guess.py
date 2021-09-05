import random

r_number = random.randint(1, 100)

easy_level = 10
hard_level = 5

def difficulty():
	level = input("Select the Difficulty Level. 'easy' or 'hard'").lower()
	if level == "hard":
		return hard_level
	else:
		return easy_level

def check_answer(guess, r_number, turn):
	if guess > r_number:
		print("Too High")
		return turn - 1
	elif guess < r_number:
		print("Too Low")
		return turn - 1
	else:
		print(f"You have gussed it right. The number is {r_number}")

print("Welcome to Guess Number")
turn = difficulty()
end_game = False
while not end_game:
	guess = 0
	if guess != r_number:
		print(f"You have {turn} guess remaining")
	
	guess = int(input("Guess: "))
	turn = check_answer(guess, r_number, turn)
	if turn == 0:
		end_game = True
		print("You've run out of guesses, you lose.")
	elif guess == r_number:
		end_game = True
	elif guess != r_number:
		print("Guess again.")