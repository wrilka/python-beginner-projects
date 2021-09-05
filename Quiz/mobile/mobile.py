class Mobile:
	def __init__ (self):
		self.model = "Real Me"
	
	def price(self, p):
		self.price = p
		print(f"You Device Model is {self.model} and price is Rs.{self.price}")
	
	def show(self, ra, ro=0):
		self.ram = ra
		self.rom = ro
		print(f"{self.model} have {self.ram}GB of RAM and {self.rom}GB of ROM.")

