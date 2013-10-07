import random as rand
import numpy as np
import sys

N = int(input('How many iterations?\t'))
ndice = input('How many dice?\t')
nsix = input('How many dice with a 6?\t')

##M = 0
##
##for i in range(N):
##    six = 0
##    for j in range(ndice):
##        # roll die no. j:
##        r = rand.randint(1, 6)
##        if r == 6:
##            six += 1
##
##    # successful event?        
##    if six >= 2:
##            M+=1
##
##p = float(M)/N
##print 'probability: ', p


## Vectorized!
eyes = np.random.randint(1, 7, (N, ndice))
compare = eyes == 6
nthrows_with_6 = np.sum(compare, axis=1)
nsuccesses = nthrows_with_6 >= nsix

M = sum(nsuccesses)
p = float(M)/N

print p


