def prime(n):
	for x in range(2, n):
		if n % x == 0:
			print(f"{n} 'equals' {x} * {n//x} .So, It's not a Prime Number")
			break
	else:
		print(f"{n} is a prime number.")
	
n= int(input("Input a number"))
prime(n)