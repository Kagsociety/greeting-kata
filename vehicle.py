class Vehicle
	sebesseg = 0
	maxspeed = 100
	def __init__(self, sebesseg, maxspeed):
		self.sebesseg = sebesseg
		self.maxspeed = maxspeed
	def accelerate(self, value):
		self.sebesseg = sebesseg+value
	def brake(self, value):
		self.sebesseg = sebesseg-value
	def status():
		print("The speed of the vehicle is", self.sebesseg)
