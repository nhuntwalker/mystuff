"""
Exercise 5.1 of Scientific Programming with Python

Given the sequence a_n = (7+1/n)/(3 - 1/n**2)
print a_n for any n.  Is there a finite limit as
n approaches infinity?

The limit appears to be 2.33333...
"""

import sys
import numpy as np

N = eval(sys.argv[1])

a_n = np.zeros(N,float)

n = 1.
while n <= N:
	a_n[n-1] = (7. + 1./n)/(3. - 1./(n**2))
	n += 1

print a_n[-1]