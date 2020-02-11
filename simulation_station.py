#!/usr/bin/env python3

# Import the Math library in order to implement the choose function
#
import math
import random

# Define the 'choose' function to use in the probability function
#


def nCr(n, k):
    f = math.factorial
    return f(n) // f(k) // f(n - k)

# Define the binomial coefficient function of error probability given a 'n' number of trials and 'k' number of errors at 'err' rate
#


def ErrProb(n, k, err):
    PROB = (nCr(n, k)) * (err**k) * ((1 - (err))**(n - k))
    return PROB

# Generate 10,000 packets of data and get the input to calculate the proabability of each packet containing zero, one two or three errors
#


def prob_Genny():
    draw = 0
    # Loop through the number of bits that could go wrong in one data packet
    for i in range(100):
        if random.random() <= 0.01:     # Set the error for each individual data packet bit being incorrect
            draw += 1
    return draw


def packets(x, y):
    packet_array = []
    for i in range(x):
        packet_array.append(prob_Genny())
    return round((sum((packet_array)) * y), 0)

# Generate the comparitve percentages
#


def percent_compare(theo, sim):
    percent_val = (abs(theo - sim) / ((theo + sim) / 2)) * 100
    return round(percent_val, 3)
