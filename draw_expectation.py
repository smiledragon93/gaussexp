import numpy as np
import matplotlib.pyplot as plt
from pylab import *
from draw_lattice import *
from arbitrary_lattice_gaussian import *

def create_box(x_1, x_2, y_2, s, num_x, num_y, precision):
    width = (num_x ) * x_1
    height = (num_y) * y_2
    x = np.arange(0, width, precision)
    y = np.arange(0, height, precision)
    X, Y = meshgrid(x, y)
    Z = exp_dist_lattice(x_1, x_2, y_2, X, Y, s, 50)
    print "Maximum distance between expectations:", Z.max()
    fig, ax = subplots()
    cnt = contour(Z, cmap=cm.YlGnBu,vmin=abs(Z).min(), vmax=abs(Z).max(), extent=[0, width, 0, height])
    (X,Y) = generate_lattice(x_1, x_2, y_2, num_x, num_y)
    plt.scatter(X,Y)
    plt.grid(True)
    plt.gca().set_aspect('equal', adjustable='box')
    plt.xticks(arange(width + 1))
    plt.yticks(arange(height))
    plt.show()
    #plt.savefig(name, bbox_inches='tight', pad_inches=0)

def read_input():
    print "Latice basis is represented by two vectors: (x1, 0)^t and (x2, y2)^t, x1 >= x2."
    try_num = 0
    x_1, x_2, y_2 = -1, -1, -1
    while not (x_1 >= x_2 and x_1 >= 0 and x_2 >= 0 and y_2 >= 0):
        if (try_num != 0):
            print "Input is incorrect. Try one more time."
        x_1 = float(input("Enter x1: "))
        x_2 = float(input("Enter x2: "))
        y_2 = float(input("Enter y2: "))
        try_num = try_num + 1
    s = float(input("Enter width of the distribution: "))
    return (x_1, x_2, y_2, s)

(x_1, x_2, y_2, s) = read_input()
create_box(x_1,x_2,y_2,s,3,3,0.05)