"""
Contains wave functions for different (n,l,m) and uses them to calculate probability
"""


import math
import matplotlib.pyplot as plt
from src.max import max1S0, max2P0, max2S0

# Value of a0
a0 = 0.0529


# dP/Vol = abs(psi) ** 2
# dP = dP * dVol


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