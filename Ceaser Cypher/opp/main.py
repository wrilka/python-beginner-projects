from alphabet import alphabets
from ceasar_cypher import Ceasar

c = Ceasar()
go_again = True
while go_again == True:
	direction = c.direction()
	text = c.text()
	shift = c.shift()
	
	ans = c.get_direction(direction, text, shift, alphabets)
	
	print(f"\nYour {direction}d word is '{ans}'\n.")
	
	
	repeat = c.repeat()
	
	go_again = c.go_again(repeat)