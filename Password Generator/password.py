import random
class Password:
	def __init__(self):
		pass
	
	def welcome(self):
		print("Welcome to Password Generator")
	
	def detail(self):
		num_of_pass = int(input("How many Password you want to generate?: "))
		print()
		letter = int(input("How many letter would you like?: "))
		number = int(input("How many Numbers would you like?: "))
		symbol = int(input("How many symbol would you like?: "))
		print()
		return letter, number, symbol, num_of_pass
	
	
	#f means find. nothing more
	def f_letter(self, let, letters):
		letter = ""
		for _ in range(let):
			letter += random.choice(letters)
		return letter
	
	def f_symbol(self, sym, symbols):
		letter = ""
		for _ in range(sym):
			letter += random.choice(symbols)
		return letter
	
	def f_number(self, num, numbers):
		letter = ""
		for _ in range(num):
			letter += random.choice(numbers)
		return letter
	
	def strong_pass(self, passw):
		password = ""
		for char in passw:
			password += char
		return password