import math
import numpy as np
import matplotlib.pyplot as plt
from pylab import *
import time
from PIL import Image

#1-dim
def gaussian_function(k, m, s):
    return math.exp(-math.pi * math.pow(k - m, 2)/(2*s*s))

def gaussian_sum(m, s, precision):
    gaussian_value = gaussian_function(0, m, s)
    sum = gaussian_value
    current_int = 1
    while (gaussian_value > precision):
        gaussian_value = gaussian_function(current_int, m, s) + gaussian_function(-1 * current_int, m, s)
        sum = sum + gaussian_value
        current_int = current_int + 1
    return sum

def expectation(m, s, precision):
    sum = gaussian_sum(m, s, precision)
    current_value = gaussian_function(1,m,s) - gaussian_function(-1,m,s)
    mean = current_value
    current_int = 2
    while (current_value > precision):
        current_value = current_int * (gaussian_function(current_int,m,s) - gaussian_function(-1*current_int,m,s))
        mean = mean + current_value
        current_int = current_int + 1
    return mean/sum


#2-dim

def gaussian_function_2_dim(x, y, m_x, m_y, s):
    squared_distance = (x - m_x) * (x - m_x) + (y - m_y) * (y - m_y)
    return np.exp(-math.pi * squared_distance/(2*s*s))

def gaussian_sum_2_dim(m_x, m_y, s, n):
    sum = 0
    for x in range(-n,n):
        for y in range(-n,n):
            sum = sum + gaussian_function_2_dim(x, y, m_x, m_y, s)
    return sum

def expectation_2_dim(m_x, m_y,s,n):
    sum = gaussian_sum_2_dim(m_x, m_y, s, n)
    expectation = [0,0]
    for x in range(-n, n):
        for y in range(-n,n):
            prob = gaussian_function_2_dim(x, y, m_x, m_y, s)/sum
            expectation[0] = expectation[0] + x * prob
            expectation[1] = expectation[1] + y * prob
    return expectation

def exp_dist(x,y,s,n):
    expectation = expectation_2_dim(x, y, 1, 100)
    dist = np.sqrt((expectation[0] - x) * (expectation[0] - x) + (expectation[1] - y) * (expectation[1] - y))
    return dist

#arbitrary lattice

def gaussian_sum_lattice(x_1, x_2, y_2, m_x, m_y, s, n):
    sum = 0
    for b_1 in range(-n, n):
        for b_2 in range(-n,n):
            x = x_1 * b_1 + x_2 * b_2
            y = y_2 * b_2
            sum = sum + gaussian_function_2_dim(x,y,m_x,m_y,s)
    return sum

def expectation_lattice(x_1, x_2, y_2, m_x, m_y, s, n):
    sum = gaussian_sum_lattice(x_1, x_2, y_2, m_x,m_y,s,n)
    expectation = [0,0]
    for b_1 in range(-n, n):
        for b_2 in range(-n,n):
            x = x_1 * b_1 + x_2 * b_2
            y = y_2 * b_2
            prob = gaussian_function_2_dim(x,y,m_x,m_y,s)/sum
            expectation[0] = expectation[0] + x * prob
            expectation[1] = expectation[1] + y * prob
    return expectation

def exp_dist_lattice(x_1, x_2, y_2, x,y,s,n):
    expectation = expectation_lattice(x_1, x_2, y_2, x, y, 1, 100)
    dist = np.sqrt((expectation[0] - x) * (expectation[0] - x) + (expectation[1] - y) * (expectation[1] - y))
    return dist

def lattice(x_1, x_2, y_2, x, y):
    if (y % y_2) != 0:
        return 0
    mult_y = y / y_2
    if (x - mult_y * x_2) % x_1 != 0:
        return 0
    return 1

def create_box(x_1, x_2, y_2, s, left, right, bottom, top, precision, name):
    x = np.arange(left, right, precision)
    y = np.arange(bottom, top, precision)
    X, Y = meshgrid(x, y)
    Z = exp_dist_lattice(x_1, x_2, y_2, X, Y, s, 100)
    #fig = imshow(Z, cmap=pl.cm.RdBu)
    fig, ax = subplots()
    cnt = contour(Z, cmap=cm.RdBu, vmin=abs(Z).min(), vmax=abs(Z).max(), extent=[0, 1, 0, 1])

    plt.axis('off')
    #fig.axes.get_xaxis().set_visible(False)
    #fig.axes.get_yaxis().set_visible(False)
    plt.savefig(name, bbox_inches='tight', pad_inches=0)



def draw_lattice_expectation(x_1, x_2, y_2, s, precision, name):
    create_box(x_1, x_2, y_2, s, 0, x_1, 0, y_2, precision, 'fbox.png')
    box_im = Image.open('fbox.png')
    box_im2 = box_im.copy()
    width, height = box_im.size
    first_box = box_im.crop((0, 0, x_2*width/x_1, height))
    second_box = box_im2.crop((x_2*width/x_1, 0, width, height))
    print second_box.size
    first_box.save('first_box.png')
    second_box.save('second_box.png')

    width_first, height_first = first_box.size
    width_second, height_second = second_box.size
    print first_box.size, second_box.size

    whole_hex = Image.new("RGB", ((width_first + width_second) * 4 + 2*width_first, height_first * 3))
    which_box = 0
    i = 0
    for y_coord in range(0, height_first * 3, height_first):
        delta_x = width_first * (2 - i)
        i = i + 1
        x_coord = 0
        for x_idx in range(0, 6, 1):
            if (which_box == 0):
                whole_hex.paste(first_box, (x_coord + delta_x, y_coord))
                x_coord = x_coord + width_first
                which_box = 1
            else:
                whole_hex.paste(second_box, (x_coord + delta_x, y_coord))
                x_coord = x_coord + width_second
                which_box = 0

    whole_hex.save(name, "PNG")
    whole_hex.save(name, "PNG")
    #cropped = whole_hex.crop((2 * width_first, 0, width*4 - 2 * width_first, height_first * 3))
    #cropped.save(name, "PNG")

#draw_lattice_expectation(3,1,1,1,0.02,'miau.png')

box = create_box(2,1,1.7,1,0,9,0,3,0.04,'true_hex.png')




