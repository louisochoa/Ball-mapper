#!/usr/bin/env python3

#@title Algorithm 3: Construction of Ball Mapper graph { form-width: "25%" }

"""
Algorithm 3 Construction of Ball Mapper graph
Input: Cover vector B(X, ε) from Algorithm 1 or 2.
V = cover elements in B(X, ε), E = ∅,
for Every point p ∈ X do
For every pair of cover elements c1 different to c2 in B(X, ε)[p], add a (weighted) edge between vertices
corresponding to the cover elements c1 and c2. Formally, E = E ∪ {c1, c2}
Return G = (V, E)
"""

##### libraries #####
import numpy as np
import matplotlib.pyplot as plt
#import matplotlib as mpl

##### input #####
E = []
from a1_greedy_ε_net import * # Cover vector B(X, ε)
# if you cannot run this line, simply copy & paste Algorithm 1 instead.

##### main #####
#if __name__ == "__main__":

for B_p in B_X: # do
    # B(p, ε)
    print(B_p)
    length = len(B_p)
    for i in range(1, length):
        for j in range(i + 1, length):
            E.append(tuple([B_p[i], distance(B_p[i], B_p[j]), B_p[j]]))

E = set(E)

"""
print()

for edge in E:
    print("({}, {}) = {}".format(edge[0], edge[2], round(edge[1], 3)))
"""


##### Plotting graph #####
# Note that even in the OO-style, we use `.pyplot.figure` to create the figure.
fig, ax = plt.subplots()  # Create a figure and an axes.

ax.set_aspect('equal', adjustable='box')

print()

for edge in E:
    run = 1
    print("{} <---{}---> {}".format(edge[0], round(edge[1], 3), edge[2]))
    if edge[0].real < edge[2].real:
        y = np.linspace(edge[0].real, edge[2].real, 2)
    elif edge[0].real > edge[2].real:
        y = np.linspace(edge[2].real, edge[0].real, 2)
    else: 
        run = 0
        print("run =", run)

    if run != 0:
        m = (edge[2].imag - edge[0].imag) / (edge[2].real - edge[0].real)
        b = edge[0].imag - edge[0].real * m
        ax.plot(y, m * y + b, label=str(round(edge[1], 3)))
    else:
        if edge[0].imag < edge[2].imag:
            plt.vlines(edge[0].real, edge[0].imag, edge[2].imag, label=str(round(edge[1], 3)))
        elif edge[0].imag > edge[2].imag:
            plt.vlines(edge[0].real, edge[2].imag, edge[0].imag, label=str(round(edge[1], 3)))
        else:
            print("WTF!!!!!!!!!!!!!!!!!!!!!!")

ax.set_xlabel('real')  # Add an x-label to the axes.
ax.set_ylabel('imaginary')  # Add a y-label to the axes.
ax.set_title("Graph of the point cloud X")  # Add a title to the axes.
ax.legend()  # Add a legend.
# "Graph of the point cloud X"
