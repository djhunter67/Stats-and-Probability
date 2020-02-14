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

# Probability of all proposed chances and the odds of winning
#
prob_winning = [None] * 9
odds_winning = [None] * 9

# The number of possible combinations of winning
#
S = nCk(69, 5) * nCk(26, 1)
#print('The number of possible combinations of winning:', round(S, 3))

# Part a: Match all 5 white balls plus the red powerball: Win the jackpot
#
prob_winning[0] = (1/(nCk(69, 5))) * (1/26)
odds_winning[0] = (prob_winning[0])**-1
print(prob_winning[0], odds_winning[0])

# Part b: Match all 5 white balls (but not the red powerball):  Win $1,000,000
#
prob_winning[1] = (1/(nCk(69, 5)))*(25/26)
odds_winning[1] = (prob_winning[1])**-1
print(prob_winning[1], odds_winning[1])

# Part c: Match 4 out of 5 white balls plus the red powerball: Win $50,000
#
prob_winning[2] = ((nCk(5, 4)*nCk(64, 1))/(nCk(69, 5))) * (1/26)
odds_winning[2] = (prob_winning[2])**-1
print(prob_winning[2], odds_winning[2])

# Part d: Match 4 white balls (but not the red powerball): win $100
#
prob_winning[3] = ((nCk(5, 4)*nCk(64, 1))/(nCk(69, 5)))
odds_winning[3] = (prob_winning[3])**-1
print(prob_winning[3], odds_winning[3])

# Part e: Match 3 white balls plus the red powerball: Win $100
#
prob_winning[4] = ((nCk(5, 3)*nCk(64, 2))/(nCk(69, 5))) * (1/26)
odds_winning[4] = (prob_winning[4])**-1
print(prob_winning[4], odds_winning[4])

# Part f: Match 3 white ball (but not the red powerball): Win $7
#
prob_winning[5] = ((nCk(5, 3)*nCk(64, 2))/(nCk(69, 5)))
odds_winning[5] = (prob_winning[5])**-1
print(prob_winning[5], odds_winning[5])

# Part g: Match 2 white balls plus the red powerball: Win $7
#
prob_winning[6] = ((nCk(5, 2)*nCk(64, 3))/(nCk(69, 5))) * (1/26)
odds_winning[6] = (prob_winning[6])**-1
print(prob_winning[6], odds_winning[6])

# Part h: Match 1 white ball plus the red powerball: Win $4
#
prob_winning[7] = ((nCk(5, 1)*nCk(64, 4))/(nCk(69, 5))) * (1/26)
odds_winning[7] = (prob_winning[7])**-1
print(prob_winning[7], odds_winning[7])

# Part i: Match the red powerball only: Win $4
#
prob_winning[8] = ((nCk(5, 0)*nCk(64, 5))/(nCk(69, 5))) * (1/26)
odds_winning[8] = (prob_winning[8])**-1
print(prob_winning[8], odds_winning[8])

# Not winning at all
#
S_not = 1 - prob_winning[0]
print(S_not)
