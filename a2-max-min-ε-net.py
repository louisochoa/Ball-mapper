#!/usr/bin/env python3

#@title Algorithm 2: Max-min ε-net #Note: It seems to take double the time and also double the code XP { form-width: "25%" }

"""
Input: Point cloud X, ε > 0
Pick arbitrary p ∈ X. C = {p}
repeat
Find point p ∈ X \ C that is farthest away from C (if there is more than one, pick any).
d = dist(p, C)
C = C ∪ {p}.
until d ≤ ε
Create initially empty cover vector B(X, ε).
for Every point p ∈ C do
For every x ∈ B(p, ε) ∩ X, add p to B(X, ε)[x].
Return B(X, ε).
"""

import random
import cmath
import math

##### input #####
X = [complex(0, 0), complex(1.19386, 0), complex(-0.751519, -0.784616),
     complex(-0.751519, 0.784616), complex(0.15459, -0.828074),
     complex(0.15459, 0.828074) ]
ε = 1

C = []
C.append(random.choice(X))

X_minus_C = X.copy()
X_minus_C.remove(C[0])
inf = 100000 # infinity

##### functions #####
def distance(*args): #Euclidean distance between a point and a another point or a set of points (complex numbers)
    if len(args) == 2:
        if isinstance(args[0], complex): # x
            if isinstance(args[1], complex): # y
                return math.sqrt((args[0].real - args[1].real) ** 2  + (args[0].imag - args[1].imag) ** 2)
            elif isinstance(args[1], list): # C
                min = inf
                for c in args[1]:
                    if isinstance(c, complex): # c
                        aux = distance(args[0], c)
                        if aux < min:
                            min = aux
                    else:
                        raise TypeError
                return min
            else:
                raise TypeError
        else:
            raise TypeError("The first entry must be a complex class type.")
    else:
        raise SyntaxError("Wrong number of arguments. \n distance takes exactly 2 arguments.")


def B(p, ε): #considering the center (p) of open balls
    B = []
    B.append("B({}, {}) ∩ X =".format(p, ε)) # just for legibility
    for x in X:
        if distance(x, p) < ε:
            B.append(x)
    return B

##### main ####
#if __name__ == "__main__":

while True: # do
    dist = 0
    p = None
    for q in X_minus_C:
        aux = distance(q, C)
        if dist < aux:
            dist = aux
            p = q
    C.append(p)
    X_minus_C.remove(p)

    if dist <= ε: # until
        break

B_X = [] # B(X, ε)

for p in C:
    B_X.append(B(p, ε)) #B(X, ε)

print("ε =", ε)
print("X =", X)
print("C =", C)
print("B(X, ε) =", B_X) #B(X, ε)
