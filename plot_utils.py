#!/usr/bin/python3

import matplotlib.pyplot as plt
import numpy as np

def plot_pose(poses):

    # Create a figure and axes
    fig, ax = plt.subplots()

    # Generate some data
    X = []
    Y = []
    thetas = []
    for pose in poses:
        X.append(pose.translation()[0]) 
        Y.append(pose.translation()[1]) 
        thetas.append(pose.theta())
    
    X = np.array(X)
    Y = np.array(Y)
    thetas = np.array(thetas)
    U = X + np.cos(thetas) * 0.01
    V = Y + np.sin(thetas) * 0.01

    print(f"X {X}\n")

    print(f"Y {Y}\n")
    # Plot the arrows
    ax.quiver(X, Y, U, V, angles='xy', scale_units='xy', scale=1)

    # Show the plot
    plt.show()