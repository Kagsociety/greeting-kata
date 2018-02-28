class Car:
	brand = "IDK yet"
	maxSpeed = 0
	def setBrand(self, x):
		self.brand = x
	def setMaxSpeed(self, x):
		self.maxSpeed = x
	def printData(self):
		print ("My car is a/an", self.brand, "and it's max speed is", self.maxSpeed)
#1
myObject = Car()
myObject.setBrand("Audi")
myObject.setMaxSpeed('200km/h')
myObject.printData()
