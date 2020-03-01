import numpy as np
import math

#a0
a0 = 0.0529


def calcP1S0(r, theta, phi):
    psi = abs( (1 / (math.sqrt(math.pi) * (a0 ** (3/2)))) * math.e ** (-r / a0))
    print(psi)
    P = psi ** 2 * 4 * math.pi * r ** 2
    return P


def calcP2S0(r, theta, phi):
    psi = abs( (1 / (4 * math.sqrt(2 * math.pi)) * a0 ** (3/2)) * (2 - r/a0) * math.e ** (-r / (2*a0)))
    print(psi)
    P = psi ** 2 * 4 * math.pi * r ** 2
    return P


def calcP2P0(r, theta, phi):
    psi = abs( (1 / (4 * math.sqrt(2 * math.pi)) * a0 ** (3/2)) * (r / a0) * math.e ** (-r / (2*a0)) * math.cos(theta))
    print(psi)
    P = psi ** 2 * 4 * math.pi * r ** 2
    return P

print("1S1")
print(calcP1S1(a0,0,0))
print("2S1")
print(calcP2S1(a0*5,0,0))
print("2P1")
print(calcP2P1(a0*4,math.pi/2,0))