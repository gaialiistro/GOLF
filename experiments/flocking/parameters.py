"""
Parameter settings to be loaded in the model
"""
from typing import List, Tuple

"""
General settings (DO NOT CHANGE)
"""
# screen settings
S_WIDTH, S_HEIGHT = 1000, 1000
SCREEN: Tuple[int, int] = (S_WIDTH, S_HEIGHT)

# choose how long to run the simulation
# -1 : infinite, N: finite
FRAMES = -1

# choose swarm type
SWARM = "Flock"
# define the number of agents
N_AGENTS = 300
# object location
OBJECT_LOC: List[float] = [S_WIDTH / 2.0, S_HEIGHT / 2.0]
CONVEX = True


# Agent Settings:
# agent size
WIDTH = 10
HEIGHT = 8
# update
dT = 0.2
# agents mass
MASS = 20
# agent maximum/minimum speed
MAX_SPEED = 7.0
MIN_SPEED = 4.0


# Boid Settings:
# velocity force
MAX_FORCE = 8.0

"""
Simulation settings to adjust:
"""

"""
Flock class parameters (defines the environment of where the flock to act)
"""
# Define the environment
OBSTACLES = True
OUTSIDE = False


"""
Boid class parameters
"""
# view of neighbor agents
RADIUS_VIEW = 70
# weights for velocity forces
COHESION_WEIGHT = 0.0
ALIGNMENT_WEIGHT = 0.0
SEPARATION_WEIGHT = 0.0
