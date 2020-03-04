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
import numpy as np
from sklearn.cluster import KMeans



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

Ps1S0=[]
for i in range(1000):
    r = i/1000
    Ps1S0.append(calcP1S0(r,0,0))
plt.plot(range(1000), Ps1S0)
plt.title("1S0")
plt.show()

Ps2S0=[]
for i in range(1000):
    r = i/1000
    Ps2S0.append(calcP2S0(r,0,0))
plt.plot(range(1000), Ps2S0)
plt.title("2S0")
plt.show()

Ps2P0=[]
for i in range(1000):
    r = i/1000
    Ps2P0.append(calcP2P0(r,math.pi/4,0))
plt.plot(range(1000), Ps2P0)
plt.title("2P0")
plt.show()









############# MAIN ############################

a0 = 0.0529
solns = []

radii = sympy.solve((-1.02157 * 10 ** 6 * math.e ** (-37.8072 * r) * (r ** 2 - 0.0529 * r)), r)
max1S0 = 10.233
for radius in radii:
    if max1S0 < calcP1S0((complex(radius)).real, 0, 0):
        max1S0 = calcP1S0((complex(radius)).real, 0, 0)

print("Max1s0 %s" % max1S0)
#MANUAL:
max2S0 = 3.6100  # at 3a0 + a0/(0.2*sqrt(5))
max2P0 = 1.9585  # at 4a0, pi/4 or 3pi/4


# r: 0 -> 10*a0, theta: 0-> pi, phi: 0 -> 2pi
def is_above_max(rmax, thetamax, phimax, threshold):
    # Create point and define x, y, z to be randoms within the proper range
    n = spherical_point()
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
        if is_above_max(10 * a0, math.pi, 2 * math.pi, 0.99):
            counter += 1

    return counter / trials


# Class point to store (r, theta, phi) coordinates
class spherical_point:
    def __init__(self):
        self.r = 0
        self.theta = 0
        self.phi = 0

    def __str__(self):
        return "(%s, %s, %s)" % (self.r, self.theta, self.phi)


mc_probability(100000)
for i in solns:
    print(i)

Rs = []
Thetas = []

for i in solns:
    Rs.append(i.r)
    Thetas.append(i.theta)

# Plot the scatter of solutions as (r, theta) points because they are phi symmetric
plt.scatter(Rs,Thetas)
plt.show()

# #####################CLUSTERING#################

num_clusters = 4

# Convert solns to an np array of (r, theta, phi) points
solns_as_nparray = []
for i in solns:
    solns_as_nparray.append((i.r, i.theta, i.phi))

solns_as_nparray = np.array(solns_as_nparray)

est = KMeans(n_clusters=num_clusters)
est.fit(solns_as_nparray)
labels = est.labels_


# Function to plot clusters that kmeans has estimated
def plot_Kmeans_clusters(ax, sample, label, k):
    colors = ['bo', 'ro', 'go', 'mo']
    for i in range(k):
        data = sample[label == i]
        ax.plot(data[:, 0], data[:, 1], colors[i])


# Plot clusters
fig, ax = plt.subplots(figsize=(8,8))
plot_Kmeans_clusters(ax, solns_as_nparray.astype(float), labels, num_clusters)
plt.title("Clustering electron orbitals")
plt.show()
