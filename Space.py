import numpy as np
from SystemState import SystemState

class Space:
    SunMass = 1.99E30
    EarthMass = 5.94E24
    GConst = 6.67E-11
    EarthRadius = 6378000

    # There are 4 variables, each of three coordinates. This function computes
    # d/dt for each variable
    def getDerivatives(self, time, state, dState):

        # Fill in this method.
        # Set dState with time derivatives of state .

        dState.EarthPostion = state.EarthPostion
        dState.EarthVelocity = state.EarthVelocity
        dState.AsteroidPostion = state.AsteroidPostion
        dState.AsteroidVelocity = state.AsteroidVelocity

    # Decides whether the simulation should terminate
    def shouldHalt(self, t_old, t_new, state_old, state_new):

        # Fill in this method.
        # Decide whether the collision of the asteroid with Earth occured.

        return False

    # This function returns a list of values which sould be constant during the simulation.
    # It is used to check the correctness of the algorithm and if the step size is not too big
    def getConservedValues(self, t, state):

        # Fill in this method.
        # Returs as much values as possible which are constant during the simulation and may help
        # us to decide if the algorithm is correct

        return [42, 69]
