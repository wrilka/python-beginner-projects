class Ceasar:
	def __init__(self):
		pass
	
	
	def direction(self):
		direction = input("Type 'encode' to encryot and 'decode' to decrypt\n").lower()
		return direction
	
	
	def text(self):
		text = input("Input your word: ").lower()
		return text
	
	
	def shift(self):
		shift = int(input("Input the shift amount: "))
		shift = shift % 26
		return shift
	
	def get_direction(self, direction, text, shift, alphabets):
		letter = ""
		for char in text:
			position = alphabets.index(char)
			if direction == "encode":
				new_position = position + shift
				letter += alphabets[new_position]
			else:
				new_position = position - shift
				letter += alphabets[new_position]
		return letter
		
	
	def repeat(self):
		repeat = input("Type 'y' to go again and 'n' to end: ").lower()
		return repeat
	
	def go_again(self, again):
		if again == "n":
			return False
		else:
			return True