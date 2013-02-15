import physicalValues

class Component():
	def __init__(self, name):
		self.name = name

class Resistor(Component):
	def __init__(self, name, resistance):
		Component.__init__(name)
		self.Resistance = Ohm(Resistance)
