class PhysicalValue():
	def __init__(self, value=0):
		self.value = value

	def __str__(self):
		return self.value

class Ohm(PhysicalValue):
	def calculate(self, V, I):
		self.value = V / I
		return self.value

class Volt(PhysicalValue):
	def calculate(self, I, R):
		self.value = I * R
		return self.value

class Ampere(PhysicalValue):
	def calculate(self, V, R):
		self.value = V / R
		return self.value

class Farad(PhysicalValue):
	pass

class Henry(PhysicalValue):
	pass

class Watt(PhysicalValue):
	pass

class Joule(PhysicalValue):
	pass
