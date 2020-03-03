"""
Contains max local values of probabilities for each of the wave functions utilized
"""

# Expect P1S0_MAX = 10.233 at a0
# Expect P1S0_MAX = 3.6100 at 3a0 + a0/(0.2*sqrt(5))
# Expect P1S0_MAX = 1.9585 at 4a0, pi/4 or 3pi/4


import math

import sympy as sympy
from sympy.abc import r, theta
import sympy

import src.Psis


# define properly wrt numerical spherical coord derivatives/concavity in the future

# Derivative of eqn for 1S0
# -1.02157×10^6 e^(-37.8072 x) (x^2 - 0.0529 x) =0
radii = sympy.solve((-1.02157 * 10 ** 6 * math.e ** (-37.8072 * r) * (r ** 2 - 0.0529 * r)), r)
max1S0 = 0
for radius in radii:
    if max1S0 < src.Psis.calcP1S0((complex(radius)).real, 0, 0):
        max1S0 = src.Psis.calcP1S0((complex(radius)).real, 0, 0)

# Derivative of eqn for 2S0
# (e^(-r/(0.0529*2))/(4*sqrt(2*pi) * 0.0529^ (3/2)) *(2-r/0.0529)) ^2 *4*pi*r^2
# e^(-18.9036 r) r (-5.70395×10^6 r^3 + 2.41391×10^6 r^2 - 255392. r + 6755.12)


#radii = sympy.solve((math.e ** (-18.9036 * r) * r * (-5.70395 * 10 ** 6 * r ** 3 + 2.41391 * 10 ** 6 * r ** 2 - 255392 * r + 6755.12)), r)

#print("radii 2s0")
#print(radii)
#max2S0 = 0
#for radius in radii:
#    if not ("I" in str(radius)):
#        if max2S0 < src.Psis.calcP2S0((complex(radius)).real, 0, 0):
#            max2S0 = src.Psis.calcP2S0((complex(radius)).real, 0, 0)

# Derivative for theta in eqn for 2P0
# (cos^2(θ) sin(θ)) → cos^3(θ) - 2 sin^2(θ) cos(θ)
# theta = pi/4 or theta = 3pi/4

#angles = sympy.solve((sympy.cos(theta) ** 3 - 2 * (sympy.sin(theta) ** 2) * sympy.cos(theta)), theta)

# Derivative for r in 2P0
# (e^(-r/(0.0529*2))/(4*sqrt(2*pi) * 0.0529^ (3/2)) *(r/0.0529) *cos(pi/4)) ^2 *2*pi*sin(pi/4)*r^2
# →e^(-18.9036 r) * r^3 *(213362. - 1.00833×10^6 r)

#max2P0 = 0
#for angle in angles:
#    for radius in radii:
#        if max2P0 < src.Psis.calcP2P0((complex(radius)).real, (angle.evalf()), 0):
#            max2P0 = src.Psis.calcP2P0((complex(radius)).real, (angle.evalf()), 0)


#MANUAL:
max2S0 = 3.6100 #at 3a0 + a0/(0.2*sqrt(5))
max2P0 = 1.9585 #at 4a0, pi/4 or 3pi/4

print("Max of 1S0")
print(max1S0)
print("Max of 2S0")
print(max2S0)
print("Max of 2P0")
print(max2P0)