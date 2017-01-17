import math

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