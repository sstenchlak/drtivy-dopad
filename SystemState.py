import numpy as np

# This class represents the state of our system containing 12 variables.
# Internally all the variables are stored in a single array, but you can
# access separately Earth's and Asteroid's positions and velocities
class SystemState:
	def __init__(self, EarthPosition=None, EarthVelocity=None, AsteroidPosition=None, AsteroidVelocity=None, vector=None):
		if (vector is not None):
			self.vector = vector
		else:
			if EarthPosition is None:
				self.vector = np.zeros(12)
			else:
				self.vector = np.concatenate((EarthPosition, EarthVelocity, AsteroidPosition, AsteroidVelocity))

	def __add__(self, other):
		return SystemState(vector=(self.vector + other.vector))

	def __mul__(self, other):
		return SystemState(vector=self.vector*other)

	def __rmul__(self, other):
		return self.__mul__(other)

	def __floordiv__(self, other):
		return SystemState(vector=self.vector / other)

	def __truediv__(self, other):
		return self.__floordiv__(other)

	@property
	def EarthPosition(self):
		return self.vector[0:3]

	@property
	def EarthVelocity(self):
		return self.vector[3:6]

	@property
	def AsteroidPosition(self):
		return self.vector[6:9]

	@property
	def AsteroidVelocity(self):
		return self.vector[9:12]

	@EarthPosition.setter
	def EarthPosition(self, value):
		self.vector[0:3] = value

	@EarthVelocity.setter
	def EarthVelocity(self, value):
		self.vector[3:6] = value

	@AsteroidPosition.setter
	def AsteroidPosition(self, value):
		self.vector[6:9] = value

	@AsteroidVelocity.setter
	def AsteroidVelocity(self, value):
		self.vector[9:12] = value

	def __str__(self):
		return "   Earth position: " + self.EarthPosition.__str__() + \
			"\n         velocity: " + self.EarthVelocity.__str__() + \
			"\nAsteroid position: " + self.AsteroidPosition.__str__() + \
			"\n         velocity: " + self.AsteroidVelocity.__str__() + \
			"\ndistance [Earths]: " + (np.linalg.norm(self.AsteroidPosition - self.EarthPosition)/6378000).__str__()
