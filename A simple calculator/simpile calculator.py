def add(n1, n2):
	return n1 + n2

def subtract(n1, n2):
	return n1 - n2

def multiply(n1, n2):
	return n1 * n2
	
def divide(n1, n2):
	return n1 / n2

operation = {
"+": add,
"-": subtract,
"*": multiply,
"/": divide
}

def calculator():
	n1 = float(input("Input the first number?:\n"))
	calculate_answer = True
	while calculate_answer:
		for symbols in operation:
			print(symbols)
		operation_symbol = input("choose the operation: \n")
		n2 = float(input("Input the next Number\n"))
		calculation = operation[operation_symbol]
		answer = calculation(n1,n2)
		
		print(f"{n1} {operation_symbol} {n2} is = {answer}")
		n3 = input(f"Do you want to continue calculating you answer {answer} Type 'y' or 'n'")
		if n3 == "y":
			n1 = answer
		else:
			calculate_answer = False
			calculator()
calculator()