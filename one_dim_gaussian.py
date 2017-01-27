import math
import matplotlib.pyplot as plt
import numpy as np

def gaussian_function(k, m, s):
    return np.exp(- math.pi * (k - m) * (k - m)/(2*s*s))

def gaussian_sum(m, s, precision):
    gaussian_value = gaussian_function(0, m, s)
    sum = gaussian_value
    current_int = 1
    #while (gaussian_value > precision):
    for i in range(0, 100):
        gaussian_value = gaussian_function(current_int, m, s) + gaussian_function(-1 * current_int, m, s)
        sum = sum + gaussian_value
        current_int = current_int + 1
    return sum

def expectation(m, s, precision):
    sum = gaussian_sum(m, s, precision)
    current_value = gaussian_function(1,m,s) - gaussian_function(-1,m,s)
    mean = current_value
    current_int = 2
    #while (current_value > precision):
    for i in range(0,100):
        current_value = current_int * (gaussian_function(current_int,m,s) - gaussian_function(-1*current_int,m,s))
        mean = mean + current_value
        current_int = current_int + 1
    return mean/sum

def draw_1d_expectation(s, name):
    X = np.arange(0,1,0.01)
    Y = X - expectation(X,s, 0.00000000001)
    plt.figure()
    plt.plot(X,Y)
    Z = Y.max() * np.sin(X*2*math.pi)
    plt.plot(X, Z)
    # plt.show()
    plt.savefig(name)
    # plt.plot(X, Z-Y)
    # plt.plot(X, (Z-Y).max() * np.sin(X*4*math.pi))
    # T = (Z-Y).max() * np.sin(X*4*math.pi) - (Z-Y)
    # plt.plot(X, T)
    # plt.show()

def draw_diff_with_sin():
    X = np.arange(0, 1, 0.01)
    exp_diff = X - expectation(X, 1, 0.00000000001)
    sine1 = exp_diff.max() * np.sin(X * 2 * math.pi)
    diff1 = sine1 - exp_diff
    plt.figure()
    plt.plot(X, diff1)
    plt.grid(True)
    plt.xticks(np.arange(0,1,0.1))
    plt.savefig("diff_with_sin_1")
    sine2 = diff1.max() * np.sin(X * 4 * math.pi)
    diff2 = diff1 - sine2
    plt.figure()
    plt.grid(True)
    plt.xticks(np.arange(0,1,0.1))
    plt.plot(X, diff2)
    plt.savefig("diff_with_sin_2")



def draw_sum(s):
    X = np.arange(0, 1, 0.01)
    Y = gaussian_sum(X, s, 0.0000000001)
    plt.plot(X,Y)
    plt.show()

draw_diff_with_sin()


# for s in np.arange(0.2,4.2,0.2):
#     name = "s="+str(s)+".png"
#     draw_1d_expectation(s, name)
