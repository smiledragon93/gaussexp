import numpy as np
import matplotlib.pyplot as plt
from pylab import *
from draw_lattice import *
from arbitrary_lattice_gaussian import *
from mpl_toolkits.mplot3d import axes3d, Axes3D

def create_box(x_1, x_2, y_2, s, num_x, num_y, precision, name):
    width = (num_x ) * x_1
    height = (num_y) * y_2
    x = np.arange(0, width, precision)
    y = np.arange(0, height, precision)
    X, Y = meshgrid(x, y)
    Z = exp_dist_lattice(x_1, x_2, y_2, X, Y, s, 50)
    print "Maximum distance between expectations:", Z.max()
    fig, ax = subplots()

    p = ax.pcolor(X, Y, Z, cmap=cm.YlGnBu, vmin=abs(Z).min(), vmax=abs(Z).max()) # extent=[0, width, 0, height])
    #cnt = contour(Z, cmap=cm.YlGnBu,vmin=abs(Z).min(), vmax=abs(Z).max(), extent=[0, width, 0, height])
    (X,Y) = generate_lattice(x_1, x_2, y_2, num_x, num_y)
    plt.scatter(X,Y)
    plt.grid(True)
    plt.gca().set_aspect('equal', adjustable='box')
    plt.xticks(arange(width + 1))
    plt.yticks(arange(height))
    #plt.show()
    plt.savefig(name, bbox_inches='tight', pad_inches=0)


def box_3d(x_1, x_2, y_2, s, num_x, num_y, precision):
    width = (num_x) * x_1
    height = (num_y) * y_2
    x = np.arange(0, width, precision)
    y = np.arange(0, height, precision)
    X, Y = meshgrid(x, y)
    Z = exp_dist_lattice(x_1, x_2, y_2, X, Y, s, 50)
    print "Maximum distance between expectations:", Z.max()
    fig = plt.figure(figsize=(8,6))

    #ax = fig.add_subplot(1,1,1, projection='3d')
    ax = Axes3D(fig)

    ax.plot_surface(X, Y, Z, rstride=4, cstride=4, alpha=0.25)
    cset = ax.contour(X, Y, Z, zdir='z', offset=-pi, cmap=cm.coolwarm)
    cset = ax.contour(X, Y, Z, zdir='x', offset=-pi, cmap=cm.coolwarm)
    cset = ax.contour(X, Y, Z, zdir='y', offset=3*pi, cmap=cm.coolwarm)

    ax.set_xlim3d(0, width)
    ax.set_ylim3d(0, height)
    # ax.set_zlim3d(-1, Z.max()+1);
    plt.show()

def generate_pictures(x_1, x_2, y_2, s_left, s_right):
    for s in range(s_left, s_right):
        current_name = "s=" + str(s)
        current_plt = create_box(x_1, x_2, y_2, s, 3, 3, 0.05, current_name)

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
    if (s == 0):
        print "Enter range of s: "
        s_left = int(input("Enter smallest s: "))
        s_right = int(input("Enter largest s: "))
        generate_pictures(x_1, x_2, y_2, s_left, s_right)
    if (s == -1):
        box_3d(x_1, x_2, y_2, 6, 3, 3,0.05)
    else:
        create_box(x_1, x_2, y_2, s, 3, 3, 0.05, "exp")


read_input()