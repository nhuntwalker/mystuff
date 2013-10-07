from math import *
import numpy as np
import matplotlib.pyplot as plt
import datetime

x0 = 100            # initial amount
p = 5               # annual interest rate
r = p/360.          # daily interest rate

## Formula for final amount after compounded interest:
## x(n) = (1 + (p/D)/100)^(n) * x(0) for n days where D = 360
##                                   for n months where D = 12
##                                   for n years where D = 1

date1 = datetime.date(2007, 8, 3)
date2 = datetime.date(2011, 8, 3)
diff = date2 - date1
N = diff.days
index_set = range(N+1)

x = np.zeros(len(index_set))    # setting up money array for N periods

# solution:
x[0] = x0   # initial amount

for n in index_set[1:]:
    x[n] = x[n-1] + (r/100.)*x[n-1]
print x

