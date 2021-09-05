import random
r_number = random.randint(1, 100)
		

def compare():
	if r_number > guess:
		return "You guessed too low"
	elif r_number < guess:
		return "You guessed too high"
	if attempt == 0:
		return "YOU LOSE! You are out of guess"
	if guess == r_number:
		return "YOU WIN! You guessed it right"

difficulty = input("Choose a difficulty Level 'easy' or 'hard: '").lower()
if difficulty == "hard":
	attempt = 5
if difficulty == "easy":
	attempt = 10

end_game = False
while not end_game:
	guess = int(input("Guess a number: "))
	
	if attempt == 0:
		end_game = True

	elif guess == r_number:
		end_game = True
	elif guess != r_number:
		attempt -= 1
	
	#print(r_number)
#	if guess != r_number:
#		print(f"You got {attempt} attempt left")
	print(compare())
