"""
Exercise 5.2 of Scientific Programming with Python

Given the sequence D_n = sin(2.**(-n))/2**(-n)
print D_n for any n.  Is there a finite limit as
n approaches infinity?

The limit appears to be 1.0, as the sine of 
any small angle is approximately equal to the 
angle itself.
"""
import numpy as np
import sys

N = eval(sys.argv[1])

D_n = np.zeros(N,float)

n = 1.
while n <= N:
	D_n[n-1] = np.sin(2.**(-n))/2.**(-n)
	n += 1

print D_n[-1]
