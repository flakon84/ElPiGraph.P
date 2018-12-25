# -*- coding: utf-8 -*-
"""
Created on Thu Jan  4 14:01:02 2018

@author : Alexis Martin
"""
import scipy
import numpy as np
import time
import PartitionData as part
import matplotlib.pyplot as plt


nData = 1000000
dim = 100
nNodes = 50
X = scipy.rand(nData, dim)
# print("X created")
ind = np.random.choice(nData, nNodes)
# print("ind created")
NodePositions = X[ind, ]
# print("NodePositions created")
XSquared = np.ndarray.reshape((X**2).sum(axis=1), (nData, 1))
# print("XSquared created")
print("Start")
t = time.time()
partition, dists = part.PartitionData(X, NodePositions, 100000, XSquared)
print(time.time()-t, "seconds")

if nData < 100000 and dim == 2:
    A = [None] * nNodes
    color = ['c', 'r', 'b', 'g', 'y', 'm', 'k']
    plt.figure(figsize=(5, 5))
    for i in range(nNodes):
        A[i] = X[partition[:, 0] == i]
        plt.plot(*zip(*A[i]), marker='.', ls='', color=color[i % 7])
    plt.plot(*zip(*NodePositions), marker='o', ls='')
