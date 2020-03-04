# Find Pmax values for the 1S0→2P0
# Use this to create a Heaviside function returning True iff P(r,theta,phi)>=85% of Pmax for one of the orbitals
# Query with MC; create set of solutions to the Heaviside in 3-space
# Cluster & Rebuild

# Check p at each orbital
# If >85% of max, append the point to a tuple called solutions

from sympy.abc import r
import sympy
import random
import math
import matplotlib.pyplot as plt


a0 = 0.0529

######################PSIS####################


# Wave function for (n, l, m) = (1, 0, 0)
def calcP1S0(r, theta, phi):
    psi = abs((1 / (math.sqrt(math.pi) * (a0 ** (3 / 2)))) * math.e ** (-r / a0))
    #print(psi)
    p = psi ** 2 * 4 * math.pi * r ** 2
    return p


# Wave function for (n, l, m) = (2, 0, 0)
def calcP2S0(r, theta, phi):
    psi = abs((1 / (4 * math.sqrt(2 * math.pi)) * a0 ** (3 / 2)) * (2 - r / a0) * math.e ** (-r / (2 * a0)))
    #print(psi)
    p = psi ** 2 * 4 * math.pi * r ** 2
    return (p * 10**8 * 3.61 / 7.911)


# Wave function for (n, l, m) = (2, 1, 0)
def calcP2P0(r, theta, phi):
    psi = abs(
        (1 / (4 * math.sqrt(2 * math.pi)) * a0 ** (3 / 2)) * (r / a0) * math.e ** (-r / (2 * a0)) * math.cos(theta))
    #print(psi)
    p = psi ** 2 * 2 * math.sin(theta) * math.pi * r ** 2
    return (p *10**8 * 1.9586 / 4.67270677)


# Print statements to verify values
print("1S0")
print(calcP1S0(a0, 0, 0))
print("2S0")
print(calcP2S0(0.27699, 0, 0))
print("2P0")
print(calcP2P0(0.2116, 0.61548, 0))

Ps2S0=[]
for i in range(1000):
    r = i/1000
    Ps2S0.append(calcP2S0(r,0,0))
plt.plot(range(1000), Ps2S0)
plt.show()

Ps2P0=[]
for i in range(1000):
    r = i/1000
    Ps2P0.append(calcP2P0(r,math.pi/4,0))
plt.plot(range(1000), Ps2P0)
plt.show()









############# MAIN ############################

a0 = 0.0529
solns = []

radii = sympy.solve((-1.02157 * 10 ** 6 * math.e ** (-37.8072 * r) * (r ** 2 - 0.0529 * r)), r)
max1S0 = 0
for radius in radii:
    if max1S0 < calcP1S0((complex(radius)).real, 0, 0):
        max1S0 = calcP1S0((complex(radius)).real, 0, 0)
#MANUAL:
max2S0 = 3.6100 #at 3a0 + a0/(0.2*sqrt(5))
max2P0 = 1.9585 #at 4a0, pi/4 or 3pi/4



# r: 0 -> 10*a0, theta: 0-> pi, phi: 0 -> 2pi
def is_above_max(rmax, thetamax, phimax, threshold):
    # Create point and define x, y, z to be randoms within the proper range
    n = point()
    n.r = random.uniform(0, rmax)
    n.theta = random.uniform(0, thetamax)
    n.phi = random.uniform(0, phimax)
    if calcP1S0(n.r, n.theta, n.phi) >= threshold * max1S0 or calcP2S0(n.r, n.theta, n.phi) >= threshold * max2S0 or calcP2P0(n.r, n.theta, n.phi) >= threshold * max2P0:
        solns.append(n)
        return True


# Takes a number of trials and a function, and checks how many random points are above max threshold
# Using check_prob
def mc_probability(trials):
    counter = 0
    for i in range(trials):
        # Fix additional zeros once check_prob is fully defined
        if is_above_max(10 * a0, math.pi, 2 * math.pi, 0.85):
            counter += 1

    return counter / trials


class point:
    def __init__(self):
        self.r = 0
        self.theta = 0
        self.phi = 0


mc_probability(1000)
print(solns)
