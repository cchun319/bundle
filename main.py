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
from transform import Transform2D
from plot_utils import plot_pose
# https://dfki-ric.github.io/pytransform3d/_auto_examples/plots/plot_convention_rotation_global_local.html#sphx-glr-auto-examples-plots-plot-convention-rotation-global-local-py




if __name__ == '__main__':
    x_0 = Transform2D(1, 0, 0)

    d_x = Transform2D(2, 0, np.deg2rad(30))

    x_1 = x_0 * d_x
    x_1r = d_x * x_0

    poses = [x_1, x_1r]

    plot_pose(poses)

    