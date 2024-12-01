#!/usr/bin/python3
'''
create grid, 20m x 20m
random points for landmarks
3 poses, with translation and rotation
2 transforms between the poses
keep the true values, find the seen lankmarks corrresponding the poses, indices, poses in cameras
'''

import numpy as np
from numpy.linalg import inv

# https://dfki-ric.github.io/pytransform3d/_auto_examples/plots/plot_convention_rotation_global_local.html#sphx-glr-auto-examples-plots-plot-convention-rotation-global-local-py

class Transform2D:
    def __init__(self, x, y, theta):
        self._translation = np.array([x, y])
        self._theta = theta # radian
        self._transform = np.array([[np.cos(self._theta), np.sin(self._theta), x],[-np.sin(self._theta), np.cos(self._theta), y],[0, 0, 1]])
    

    def translation(self):
        return self._transform[0:2, 2]

    def rotation(self):
        return self._transform[0:2, 0:2]

    def theta(self):
        return self._theta
    
    def inv(self):
        pass

    @classmethod
    def from_transform(cls, name):
        return cls(open(name, 'rb'))

    def __mul__(self, other):
        print('__mul__')
        result = np.matmul(self._transform, other._transform)
        return Transform2D(result[2,0], result[2,1], np.arctan2(result[0,1], result[0,0]))

    def __rmul__(self, other):
        print('__rmul__')
        return other

    def __str__(self):
        print("not yet implemenat")
        pass
