#!/usr/bin/env python3

#@title Algorithm 1: Greedy ε-net ##### { form-width: "25%" }

"""
Input: Point cloud X, ε > 0
Mark all points in X as not covered.
Create initially empty cover vector B(X, ε).
repeat
Pick a first point p ∈ X that is not covered.
For every point in x ∈ B(p, ε) ∩ X, add p to B(X, ε)[x].
until All elements of X are covered.
return B(X, ε).
"""

import cmath
import math

##### input #####
X = [complex(0, 0), complex(1.19386, 0), complex(-0.751519, -0.784616),
     complex(-0.751519, 0.784616), complex(0.15459, -0.828074),
     complex(0.15459, 0.828074) ]
ε = 1
B_X = [] # B(X, ε)

##### functions #####
def distance(x, y): #Euclidean distance between points (complex numbers)
    return math.sqrt((x.real - y.real) ** 2  + (x.imag - y.imag) ** 2)

def B(p, ε): #considering the center (p) of open balls
    B = []
    B.append("B({}, {}) ∩ X =".format(p, ε)) # just for legibility
    for x in X:
        if distance(x, p) < ε:
            B.append(x)
    return B

##### main ####
#if __name__ == "__main__":

for p in X: # while
    B_X.append(B(p, ε)) #B(X, ε)

print("ε =", ε)
print("X =", X)
print("B(X, ε) =", B_X) #B(X, ε)
