from math import *
import numpy as np
import sys

N = int(sys.argv[1])
#x = np.zeros(N+1, int)
xnm1 = 1
xnm2 = 1
n = 2
while n <= N:
    xn = xnm1 + xnm2
    print 'x_%d = %d' % (n, xn)
    xnm2 = xnm1
    xnm1 = xn
    n += 1
