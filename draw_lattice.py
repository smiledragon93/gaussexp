import math
import numpy as np
import matplotlib.pyplot as plt
from pylab import *

def lattice(x_1, x_2, y_2, x, y):
    if (y % y_2 != 0):
        return 0
    mult_y = y / y_2
    if (x - mult_y * x_2) % x_1 != 0:
        return 0
    return 1

def generate_lattice(x_1, x_2, y_2, width, height):
    X = []
    Y = []
    for horizontal_idx in range(0, width):
        for vertical_idx in range(0, height):
            x = horizontal_idx * x_1 + vertical_idx * x_2
            y = vertical_idx * y_2
            X.append(x)
            Y.append(y)
    return (X, Y)


