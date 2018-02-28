class Person:
	# attributes (tagvaltozok)
	name = "No name yet"
	age = 0
	# methods (fuggvenyek)
	def setName(self, x):
		self.name = x
	def setAge(self, x):
		self.age = x
	def talk(self):
		print("Hi! My name is", self.name, "and I am", self.age, "years old.")
#1
myObject = Person()
myObject.setName("Peter")
myObject.setAge(22)
myObject.talk()
#2
someObject = Person()
someObject.setName("Sandra")
someObject.setAge(35)
someObject.talk()
