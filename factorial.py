def factorial(n):
	if n < 0:
		return None

	if n < 2:
		return 1

	return n * factorial(n - 1)
	
n = int(input("Enter a number to find its factorial: "))
print(n ,'factorial is: ', factorial(n))				

