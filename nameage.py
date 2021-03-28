class person:
	fname = None
	lname = None
	age = None

	def get_fname(self):
		self.fname = input("Enter your first name: ")
	def get_lname(self):
		self.lname = input("Enter your last name: ")
	def get_age(self):
		self.age = input("Enter your age: ")

	def print_fname(self):
		print("Your first name is: ", self.fname)

	def print_lname(self):
		print("Your last name is: ", self.lname)
		
	def print_age(self):
		print("Your age is: ", self.age)
		
# creatin a constructor for the class above
person1 = person()
person1.get_fname()
person1.get_lname()
person1.get_age()
person1.print_fname()
person1.print_lname()
person1.print_age()			
										
