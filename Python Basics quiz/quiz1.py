## Exercise 1: Given two integer numbers return their product. If the product is greater than 1000, then return their sum

# create a function for logic.
def func_decider(int1, int2):

	product = int1 * int2

	if product <= 1000:
		return product
	else:
		return int1 + int2	

# get input from user.
int1 = int(input("Enter first number: "))
int2 = int(input("Enter second number: "))

# create constructor to reference the function
determiner = func_decider(int1, int2)
print("The outcome is: ", determiner)