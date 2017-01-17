import numpy as np
import matplotlib.pyplot as plt
from pylab import *
from draw_lattice import *
from arbitrary_lattice_gaussian import *

def create_box(x_1, x_2, y_2, s, num_x, num_y, precision, name):
    width = (num_x + 1) * x_1
    height = num_y * y_2
    x = np.arange(0, width, precision)
    y = np.arange(0, height, precision)
    X, Y = meshgrid(x, y)
    Z = exp_dist_lattice(x_1, x_2, y_2, X, Y, s, 100)
    fig, ax = subplots()
    cnt = contour(Z, cmap=cm.RdBu,vmin=abs(Z).min(), vmax=abs(Z).max(), extent=[0, width, 0, height])
    (X,Y) = generate_lattice(x_1, x_2, y_2, num_x, num_y)
    plt.scatter(X,Y)
    plt.grid(True)
    plt.gca().set_aspect('equal', adjustable='box')
    plt.xticks(arange(width + 1))
    plt.yticks(arange(height + 1))
    plt.show()
    plt.savefig(name, bbox_inches='tight', pad_inches=0)

box = create_box(2,1,1.7,1,9,4,0.04,'true_hex1.png')