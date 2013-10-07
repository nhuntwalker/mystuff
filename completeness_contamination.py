import numpy as np
import matplotlib.pyplot as plt

a = 0.1
N = 1E6
mu1, sig1 = 150.,12.
x1 = np.random.normal(mu1,sig1,N)
mu2, sig2 = 100.,10.
x2 = np.random.normal(mu2,sig2,N)
xc = 120.

spurious = np.where(x2 >= xc)
missed = np.where(x1 < xc)
nsource = N*a - len(missed[0]) + len(spurious[0])
completeness = (N*a - len(missed[0]))/(N*a)
contamination = len(spurious[0])/float(nsource)
print completeness, contamination
print nsource
print len(missed[0]),len(spurious[0])

