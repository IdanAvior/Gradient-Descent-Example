# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a basic script demonstrating the gradient descent algorithm on a convex function.
"""

import numpy as np
import matplotlib.pyplot as plt

def func(x):
    return x**2

def grad(x):
    return 2*x

x = np.arange(-5,5,0.00001)
plt.plot(x,func(x))
theta = -8  # starting point
alpha = 0.2 # step size
max_iter = 100
iteration = 0
while (iteration < max_iter):
    theta = theta - alpha*grad(theta)
    print("Current theta value: " + str(theta))
    if (iteration < max_iter -1):
        plt.plot(theta,func(theta),'ro')
    else:
        plt.plot(theta,func(theta),'ko')
    iteration = iteration + 1
    
print("\nFinal theta value: " + str(theta))
    
