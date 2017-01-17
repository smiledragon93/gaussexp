import numpy as np
import matplotlib.pyplot as plt
from pylab import *
from draw_lattice import *
from arbitrary_lattice_gaussian import *
from PIL import Image

def create_box(x_1, x_2, y_2, s, width, height, precision, name):
    x = np.arange(0, width, precision)
    y = np.arange(0, height, precision)
    X, Y = meshgrid(x, y)
    Z = exp_dist_lattice(x_1, x_2, y_2, X, Y, s, 100)
    fig, ax = subplots()
    cnt = contour(Z, cmap=cm.RdBu,vmin=abs(Z).min(), vmax=abs(Z).max(), extent=[0, 9, 0, 4])
    (X,Y) = generate_lattice(x_1, x_2, y_2, 5, 3)
    plt.scatter(X,Y)
    plt.grid(True)
    plt.axis('off')
    plt.show()
    plt.savefig(name, bbox_inches='tight', pad_inches=0)



# def draw_lattice_expectation(x_1, x_2, y_2, s, precision, name):
#     create_box(x_1, x_2, y_2, s, 0, x_1, 0, y_2, precision, 'fbox.png')
#     box_im = Image.open('fbox.png')
#     box_im2 = box_im.copy()
#     width, height = box_im.size
#     first_box = box_im.crop((0, 0, x_2*width/x_1, height))
#     second_box = box_im2.crop((x_2*width/x_1, 0, width, height))
#     print second_box.size
#     first_box.save('first_box.png')
#     second_box.save('second_box.png')
#
#     width_first, height_first = first_box.size
#     width_second, height_second = second_box.size
#     print first_box.size, second_box.size
#
#     whole_hex = Image.new("RGB", ((width_first + width_second) * 4 + 2*width_first, height_first * 3))
#     which_box = 0
#     i = 0
#     for y_coord in range(0, height_first * 3, height_first):
#         delta_x = width_first * (2 - i)
#         i = i + 1
#         x_coord = 0
#         for x_idx in range(0, 6, 1):
#             if (which_box == 0):
#                 whole_hex.paste(first_box, (x_coord + delta_x, y_coord))
#                 x_coord = x_coord + width_first
#                 which_box = 1
#             else:
#                 whole_hex.paste(second_box, (x_coord + delta_x, y_coord))
#                 x_coord = x_coord + width_second
#                 which_box = 0
#
#     whole_hex.save(name, "PNG")
#     whole_hex.save(name, "PNG")
    #cropped = whole_hex.crop((2 * width_first, 0, width*4 - 2 * width_first, height_first * 3))
    #cropped.save(name, "PNG")

#draw_lattice_expectation(3,1,1,1,0.02,'miau.png')

box = create_box(2,1,1.7,1,9,4,0.04,'true_hex1.png')