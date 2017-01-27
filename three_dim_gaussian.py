import numpy as np
import matplotlib.pyplot as plt
from pylab import *
from draw_lattice import *
from arbitrary_lattice_gaussian import *
from mpl_toolkits.mplot3d import axes3d, Axes3D
import time


def gaussian_function_3_dim(x, y, z,  m_x, m_y, m_z, s):
    squared_distance = (x - m_x) * (x - m_x) + (y - m_y) * (y - m_y) + (z - m_z) * (z - m_z)
    return np.exp(-math.pi * squared_distance/(2*s*s))

def gaussian_sum_3_dim_lattice(x_1, x_2, x_3, y_2, y_3, z_3, m_x, m_y, m_z, s, n):
    sum = 0
    for b_1 in range(-n, n):
        for b_2 in range(-n,n):
            for b_3 in range(-n, n):
                x = x_1 * b_1 + x_2 * b_2 + x_3 * b_3
                y = y_2 * b_2 + y_3 * b_3
                z = z_3 * b_3
                sum = sum + gaussian_function_3_dim(x,y,z,m_x,m_y, m_z, s)
    return sum

def expectation_3_dim_lattice(x_1, x_2, x_3, y_2, y_3, z_3, m_x, m_y, m_z, s, n):
    sum = gaussian_sum_3_dim_lattice(x_1, x_2, x_3, y_2, y_3, z_3, m_x, m_y, m_z, s, n)
    expectation = [0, 0, 0]
    for b_1 in range(-n, n):
        for b_2 in range(-n,n):
            for b_3 in range(-n, n):
                x = x_1 * b_1 + x_2 * b_2 + x_3 * b_3
                y = y_2 * b_2 + y_3 * b_3
                z = z_3 * b_3
                prob = gaussian_function_3_dim(x,y,z,m_x,m_y,m_z,s)/sum
                expectation[0] = expectation[0] + x * prob
                expectation[1] = expectation[1] + y * prob
                expectation[2] = expectation[2] + z * prob
    sys.stdout.write('.')
    sys.stdout.flush()
    return expectation

def exp_dist_3_dim_lattice(x_1, x_2, x_3, y_2, y_3, z_3, x,y, z, s,n):
    expectation = expectation_3_dim_lattice(x_1, x_2, x_3, y_2, y_3, z_3, x, y, z, s, n)
    print
    dist = np.sqrt((expectation[0] - x) * (expectation[0] - x) + (expectation[1] - y) * (expectation[1] - y) +
                   (expectation[2] - z) * (expectation[2] - z))
    return dist

def draw_3d_lattice(x_1, x_2, x_3, y_2, y_3, z_3, s, plane, shift, partition, name):
    if (plane == 'x'):
        x = shift
        y = np.arange(0, y_2 * 2, partition)
        z = np.arange(0, z_3 * 2, partition)
        Y,Z = meshgrid(y, z)
        f = exp_dist_3_dim_lattice(x_1, x_2, x_3, y_2, y_3, z_3, x, Y, Z, s, 35)
    if (plane == 'y'):
        y = shift
        x = np.arange(0, x_1 * 2, partition)
        z = np.arange(0, z_3 * 2, partition)
        Y,Z = meshgrid(x, z)
        f = exp_dist_3_dim_lattice(x_1, x_2, x_3, y_2, y_3, z_3, Y, y, Z, s, 35)
    if (plane == 'z'):
        z = shift
        y = np.arange(0, y_2 * 2, partition)
        x = np.arange(0, x_1 * 2, partition)
        Y, Z = meshgrid(x, y)
        f = exp_dist_3_dim_lattice(x_1, x_2, x_3, y_2, y_3, z_3, Y, Z, z, s, 35)

    print "Maximum distance between expectations:", f.max()
    fig, ax = subplots()
    p = ax.pcolor(Y, Z, f, cmap=cm.YlGnBu, vmin=abs(f).min(), vmax=abs(f).max())
    plt.grid(True)
    plt.gca().set_aspect('equal', adjustable='box')
    plt.xticks(arange(2 * y_2 ))
    plt.yticks(arange(2 * z_3))
    plt.savefig(name, bbox_inches='tight', pad_inches=0)


for s in [0.1]:
    for shift in [0]:
        name = "x:s=" + str(s) + ",shift=" + str(shift) + ".png"
        draw_3d_lattice(3, 0, 0, 2, 0, 1, s, 'x', shift, 0.05, name)
        print name





