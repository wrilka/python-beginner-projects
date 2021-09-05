from password import Password
from data import letters, numbers, symbols
import random

p = Password()
p.welcome()

letter, number, symbol, num_of_pass = p.detail()
let = letter
num = number
sym = symbol
how_many = num_of_pass

first = 0
while how_many != 0:
	how_many -= 1
	first += 1
	low_p = []
	low_p += p.f_letter(let, letters)
	low_p += p.f_number(num, numbers)
	low_p += p.f_symbol(sym, symbols)
	
	random.shuffle(low_p)
	final_pass = p.strong_pass(low_p)
	print(f"Here's your {first} final password: {final_pass}")
	
	if how_many == 0:
		break