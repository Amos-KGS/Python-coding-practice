# Exercise 3: Given a string, display only those characters which are present at an even index number.

def even_characters(nword):
	# I've started indexing at 0,you can choose to start at 1.
	for i in range(0, len(nword)-1, 2):
		print("Character at index ","[",i,"]", nword[i])

nword = str(input("Enter a word to get chatracters in even positions: "))
result = even_characters(nword)