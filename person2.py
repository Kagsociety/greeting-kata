class Person_2:
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
	def __init__(self, name="", age=''):
		self.name = name
		self.age = age
