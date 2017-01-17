import math
from two_dim_gaussian import *
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