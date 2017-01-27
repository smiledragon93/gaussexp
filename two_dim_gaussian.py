import math
import numpy as np
from one_dim_gaussian import *

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
    expectation = expectation_2_dim(x, y, s, 100)
    dist = np.sqrt((expectation[0] - x) * (expectation[0] - x) + (expectation[1] - y) * (expectation[1] - y))
    return dist