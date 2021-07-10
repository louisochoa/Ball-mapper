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

from a1_greedy_ε_net import * # if you cannot run this line, simply copy & paste Algorithm 1 instead.

##### input #####
E = []

##### main ####
#if __name__ == "__main__":

for B_p in B_X: # do
    # B(p, ε)
    print(B_p)
    length = len(B_p)
    print("length:", length)
    for i in range(1, length):
        for j in range(i + 1, length):
            E.append([B_p[i], distance(B_p[i], B_p[j]), B_p[j]])

for edge in E:
    print("{} --{}--> {}".format(edge[0], edge[1], edge[2]))
