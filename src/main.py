# Find Pmax values for the 1S0→2P0
# Use this to create a Heaviside function returning True iff P(r,theta,phi)>=85% of Pmax for one of the orbitals
# Query with MC; create set of solutions to the Heaviside in 3-space
# Cluster & Rebuild

# Check p at each orbital
# If >85% of max, append the point to a tuple called solutions

import random
import math

a0 = 0.0529


# r: 0 -> 10*a0, theta: 0-> pi, phi: 0 -> 2pi
def check_prob(r, theta, phi, function):
    num = 1000
    for i in range(num):
        # Create point and define x, y, z to be randoms within the proper range
        n = point()
        n.r = random.uniform(0, 10 * a0)
        n.theta = random.uniform(0, math.pi)
        n.phi = random.uniform(0, 2 * math.pi)

        return function(n.r, n.theta, n.phi) >= .85*max(function)


class point:
    def __init__(self):
        self.r = 0
        self.theta = 0
        self.phi = 0
