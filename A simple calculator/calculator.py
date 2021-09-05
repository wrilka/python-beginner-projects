def add(n1, n2):
	return n1 + n2

def subtract(n1, n2):
	return n1 - n2

def multiply(n1, n2):
	return n1 * n2
	
def divide(n1, n2):
	return n1 / n2

def exponent(n1, n2):
	return n1 ** n2

operation = {
"+": add,
"-": subtract,
"*": multiply,
"/": divide,
"**": exponent
}


n1 = int(input("Input the first number?:\n"))
for symbols in operation:
	print(symbols)
operation_symbol = input("Input the operation: \n")
n2 = int(input("Input another Number\n"))
calculation = operation[operation_symbol]
answer = calculation(n1,n2)

print(f"{n1} {operation_symbol} {n2} is = {answer}")