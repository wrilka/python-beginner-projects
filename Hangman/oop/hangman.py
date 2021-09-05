class Hang:
	def __init__(self):
		pass
	
	def show_bracket(self, all_word):
		self.bracket = []
		for _ in range(len(all_word)):
			self.bracket += "_"
		print(self.bracket)
		return self.bracket
	
	
	def check_word(self, user_words, r_word):
		for char in range(len(r_word)):
			word = r_word[char]
			if user_words == word:
				self.bracket[char] = user_words
		return self.bracket
	
	
	
