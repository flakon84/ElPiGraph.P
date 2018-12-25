# -*- coding: utf-8 -*-
"""
Created on Mon Feb  5 13:46:32 2018

@author: Alexis Martin
"""

from .computeElasticPrincipalGraph import computeElasticPrincipalGraph
from .PCA import PCA
import numpy as np


def computeElasticPrincipalCircle(data, NumNodes, newDim=None,
                                  drawPCAview=True,
                                  drawAccuracyComplexity=True, drawEnergy=True,
                                  Lambda=0.01, Mu=0.1, ComputeMSEP=False,
                                  MaxBlockSize=100000, TrimmingRadius=np.inf,
                                  MaxNumberOfIterations=10, eps=0.01,
                                  verbose=True,nReps=1,ProbPoints=1):
    NodeP = np.zeros((4, data.shape[1]))
    v, u, s = PCA(data)
    mn = data.mean(axis=0)
    v1 = v[:, 0]/np.linalg.norm(v[:, 0])
    v2 = v[:, 1]/np.linalg.norm(v[:, 1])
    st1 = np.std(u[:, 0], ddof=1)
    st2 = np.std(u[:, 1], ddof=1)
    NodeP[0, :] = mn - np.dot(st1, v1.T) - np.dot(st2, v2.T)
    NodeP[1, :] = mn - np.dot(st1, v1.T) + np.dot(st2, v2.T)
    NodeP[2, :] = mn + np.dot(st1, v1.T) + np.dot(st2, v2.T)
    NodeP[3, :] = mn + np.dot(st1, v1.T) - np.dot(st2, v2.T)
    ed = np.array([[0, 1], [2, 3], [1, 2], [3, 0]])
    return computeElasticPrincipalGraph(data, NumNodes, newDim,
                                            drawPCAview,
                                            drawAccuracyComplexity,
                                            drawEnergy, Lambda,
                                            Mu, NodeP, ed,
                                            np.array([["bisectedge"]]),
                                            np.array([]), ComputeMSEP,
                                            MaxBlockSize, TrimmingRadius,
                                            MaxNumberOfIterations, eps,
                                            verbose,nReps,ProbPoints,Topo="Circle")
