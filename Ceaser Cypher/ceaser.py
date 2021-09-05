alphabet= ["a", "b", "c", "d", "e", "f", "g", "h", "i", "j", "k", "l", "m", "n", "o", "p", "q", "r", "s", "t", "u", "v", "w", "x", "y", "z", "a", "b", "c", "d", "e", "f", "g", "h", "i", "j", "k", "l", "m", "n", "o", "p", "q", "r", "s", "t", "u", "v", "w", "x", "y", "z" ]

def ceasar(start_text, shift, cipher_direction):
	text=""
	for letter in start_text:
		position = alphabet.index(letter)
		if cipher_direction == "decode":
			new_position = position - shift
			new_word = alphabet[new_position]
			text += new_word
		elif cipher_direction == "encode":
			new_position = position + shift
			new_word= alphabet[new_position]
			text += new_word
	print(f"You {cipher_direction}d message is {text}")

again = True
while again:
	direction= input("Type 'encode' to Encrypt and 'decode' to decrypt:\n")
	text= input("Type your message\n").lower()
	shift= int(input("Type the shift number\n"))
	
	shift= shift % 26
	
	ceasar(start_text=text, shift=shift, cipher_direction=direction)
	
	repeat = input("Type 'Yes' to go again and 'No' to stop it").lower()
	if repeat == "no":
		again = False