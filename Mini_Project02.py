#!/usr/bin/env python3.8
"""
Christerpher Hunter 2020 FEB 13
EEE 350 Mini Project 2
ASU ID: 1201152983
"""

import math


# The choose function
#
def nCk(n, k):
    f = math.factorial
    return f(n) // f(k) // f(n - k)


# Probability of all proposed chances and the odds of winning
#
prob_winning = [None] * 9
odds_winning = [None] * 9

# Part a: Match all 5 white balls plus the red powerball: Win the jackpot
#
prob_winning[0] = (1/(nCk(69, 5))) * (1/26)
odds_winning[0] = (prob_winning[0])**-1
print('\nThe probability of winning the jackpot is '
      + str(round(prob_winning[0], 12)) + ' and the odds of winning the jackpot is ' + str(round(odds_winning[0])))
print('1 :', round(odds_winning[0]))

# Part b: Match all 5 white balls (but not the red powerball):  Win $1,000,000
#
prob_winning[1] = (1/(nCk(69, 5)))*(25/26)
odds_winning[1] = (prob_winning[1])**-1
print('\nThe probability of winning the $1,000,000 is '
      + str(round(prob_winning[1], 11)) + ' and the odds of winning the $1,000,000 is ' + str(round(odds_winning[1], 3)))
print('1 :', round(odds_winning[1]))

# Part c: Match 4 out of 5 white balls plus the red powerball: Win $50,000
#
prob_winning[2] = ((nCk(5, 4)*nCk(64, 1))/(nCk(69, 5))) * (1/26)
odds_winning[2] = (prob_winning[2])**-1
print('\nThe probability of winning the $50,000 is '
      + str(round(prob_winning[2], 9)) + ' and the odds of winning the $50,000 is ' + str(round(odds_winning[2], 3)))
print('1 :', round(odds_winning[2]))

# Part d: Match 4 white balls (but not the red powerball): win $100
#
prob_winning[3] = ((nCk(5, 4)*nCk(64, 1))/(nCk(69, 5)))
odds_winning[3] = (prob_winning[3])**-1
print('\nThe probability of winning $100 is '
      + str(round(prob_winning[3], 8)) + ' and the odds of winning $100 is ' + str(round(odds_winning[3], 3)))
print('1 :', round(odds_winning[3]))

# Part e: Match 3 white balls plus the red powerball: Win $100
#
prob_winning[4] = ((nCk(5, 3)*nCk(64, 2))/(nCk(69, 5))) * (1/26)
odds_winning[4] = (prob_winning[4])**-1
print('\nThe probability of winning $100 and the red ball is '
      + str(round(prob_winning[4], 8)) + ' and the odds of winning $100 is ' + str(round(odds_winning[4], 3)))
print('1 :', round(odds_winning[4]))

# Part f: Match 3 white ball (but not the red powerball): Win $7
#
prob_winning[5] = ((nCk(5, 3)*nCk(64, 2))/(nCk(69, 5)))
odds_winning[5] = (prob_winning[5])**-1
print('\nThe probability of winning $7 is '
      + str(round(prob_winning[5], 6)) + ' and the odds of winning $7 is ' + str(round(odds_winning[5], 3)))
print('1 :', round(odds_winning[5]))

# Part g: Match 2 white balls plus the red powerball: Win $7
#
prob_winning[6] = ((nCk(5, 2)*nCk(64, 3))/(nCk(69, 5))) * (1/26)
odds_winning[6] = (prob_winning[6])**-1
print('\nThe probability of winning $7 and getting the red ball is '
      + str(round(prob_winning[6], 6)) + ' and the odds of winning $7 is ' + str(round(odds_winning[6], 3)))
print('1 :', round(odds_winning[6]))

#
prob_winning[7] = ((nCk(5, 1)*nCk(64, 4))/(nCk(69, 5))) * (1/26)
odds_winning[7] = (prob_winning[7])**-1
print('\nThe probability of winning the jackpot is '
      + str(round(prob_winning[7], 5)) + ' and the odds of winning the jackpot is ' + str(round(odds_winning[7], 3)))
print('1 :', round(odds_winning[7]))

# Part i: Match the red powerball only: Win $4
#
prob_winning[8] = ((nCk(5, 0)*nCk(64, 5))/(nCk(69, 5))) * (1/26)
odds_winning[8] = (prob_winning[8])**-1
print('\nThe probability of winning the jackpot is '
      + str(round(prob_winning[8], 5)) + ' and the odds of winning the jackpot is ' + str(round(odds_winning[8], 3)))
print('1 :', round(odds_winning[8]))

# Not winning at all
#
S_not = 1 - prob_winning[0]
print('\nThe probability of not winning any money at all is ' + str(round(S_not, 9)))
print('1 :', S_not)

print('\nThe idea behind every caculation was to use the choose function to calculate the five balls needed to win, to choose the number of balls required in order to win that specific prize. \nMultiply that function by the total number of balls minus the five needed to win and choose the remaining number of white balls that aren\'t needed to win that specific prize. \nThose two functions over the entire possible number of winning combinations in order to get the probability.  \nWhen a red ball is concerned, the probability of one red ball is mulitiplied by the probability of the x number of winning white balls at the specific prize level asked.')
