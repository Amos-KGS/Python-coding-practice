# Exercise 2: Given a range of the first 10 numbers, Iterate from the start number to the end number,
# and In each iteration print the sum of the current number and previous number

def range_sum(n):
	num_before = 0

	for i in range(n):
		sum1 = num_before + i
		print("Number before is ", num_before, "Number after is",i, "and sum is: ", sum1)
		num_before = i

n = int(input("Enter the range of numbers: "))
result = range_sum(n)
