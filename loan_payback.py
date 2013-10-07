from math import *
import numpy as np

x0 = 12000.00
p = 5.
r = p/12.

N = 60 #(over 5 years)
index_set = range(N+1)
x = np.zeros(len(index_set))
y = np.zeros(len(index_set))

x[0] = x0
y[0] = 0

fmt = '%.2f'
for n in index_set[1:]:
    y[n] = float(fmt % ((r/100.)*x[n-1] + x0/N))
    x[n] = float(fmt % (x[n-1] + (r/100.)*x[n-1] - y[n]))

print x
print y

