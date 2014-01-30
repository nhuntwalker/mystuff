"""
Exercise 5.3 of Scientific Programming with Python

Given the sequence D_n = (f(x+h) - f(x))/h
h = 2**(-n)

make a function D(f, x, N) that takes a function
f(x), a value x, and the number N of terms in the
sequence as arguments, and returns an array with the
D_n valuees for n=0,1,...,N-1.  Make a call to the 
D function with f(x) = sin(x), x=0, and N=80.

Plot the evolution of the computed D_n values, using
small circles for data points.

Make another call to D where x = pi and plot this
sequence in a separate figure.  What would be your 
expected limit?  Why do the computations go wrong for large N?
"""
import sys
import numpy as np
import matplotlib.pyplot as plt

N = eval(sys.argv[1])

def D(f, x, N):
	D_n = np.zeros(N,float)
	n = 1.
	while n <= N:
		h = 2**(-n)
		D_n[n-1] = (f(x+h) - f(x))/h
		n += 1

	return D_n

func1 = D(np.sin,x=0,N=N)
func2 = D(np.sin,x=np.pi,N=N)

xarr = np.arange(1,N+1)

plt.subplot(121)
plt.plot(xarr,func1,linestyle='-',markersize=2,marker='o')

plt.subplot(122)
plt.plot(xarr,func1,linestyle='-',markersize=2,marker='o')

plt.show()

