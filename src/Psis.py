import numpy as np
import math

# Value of a0
a0 = 0.0529


# dP/Vol = abs(psi) ** 2
# dP = dP * dVol


# Wave funtion for (n, l, m) = (1, 0, 0)
def calcP1S0(r, theta, phi):
    psi = abs((1 / (math.sqrt(math.pi) * (a0 ** (3 / 2)))) * math.e ** (-r / a0))
    print(psi)
    p = psi ** 2 * 4 * math.pi * r ** 2
    return p


# Wave funtion for (n, l, m) = (2, 0, 0)
def calcP2S0(r, theta, phi):
    psi = abs((1 / (4 * math.sqrt(2 * math.pi)) * a0 ** (3 / 2)) * (2 - r / a0) * math.e ** (-r / (2 * a0)))
    print(psi)
    p = psi ** 2 * 4 * math.pi * r ** 2
    return p


# Wave funtion for (n, l, m) = (2, 1, 0)
def calcP2P0(r, theta, phi):
    psi = abs(
        (1 / (4 * math.sqrt(2 * math.pi)) * a0 ** (3 / 2)) * (r / a0) * math.e ** (-r / (2 * a0)) * math.cos(theta))
    print(psi)
    p = psi ** 2 * 4 * math.pi * r ** 2
    return p


# Print statements to verify values
print("1S1")
print(calcP1S0(a0, 0, 0))
print("2S1")
print(calcP2S0(a0 * 5, 0, 0))
print("2P1")
print(calcP2P0(a0 * 4, math.pi / 2, 0))
