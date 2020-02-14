#!/usr/bin/env python3.8

import math

# The choose function
#


def nCk(n, k):
    f = math.factorial
    return f(n) // f(k) // f(n - k)


# Total number of white ball in circulation
#
white_balls = []
for i in range(69):
    white_balls.append(i)

# Number of "Power Balls"
#
power_balls = []
for i in range(26):
    power_balls.append(i)
print(power_balls)
