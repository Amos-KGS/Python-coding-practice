# Your task here is very special: you must design a vowel eater! Write a program that uses:

# a for loop;
# the concept of conditional execution (if-elif-else)
# the continue statement.
# Your program must:

# ask the user to enter a word;
# use userWord = userWord.upper() to convert the word entered by the user to upper case;
# use conditional execution and the continue statement to "eat" the following vowels A, E, I, O, U from the inputted word;
# print the uneaten letters to the screen, each one of them on a separate line.

wordwithoutvowels = ""
word = input("Enter a word: ")
userWord = word.upper()

for letter in userWord:
	if letter == "A":
		continue

	elif letter == "E":
		continue
	
	elif letter == "I":
		continue
	
	elif letter == "O":
		continue
	
	elif letter == "U":
		continue
	
	else:
		wordwithoutvowels+= letter

		print(wordwithoutvowels)					
