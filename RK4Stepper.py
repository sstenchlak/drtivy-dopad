import numpy as np
from SystemState import SystemState

class RK4Stepper:

	def __init__(self):
		self.k1 = SystemState()
		self.k2 = SystemState()
		self.k3 = SystemState()
		self.k4 = SystemState()

	# Do single RK4 step.
	def nextStep(self, t_0, t_step, state, problem):

		# Fill in this method. It should return new system state after one state.
		# Use RK4

		return SystemState()