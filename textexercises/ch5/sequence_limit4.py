"""
Exercise 5.4 of Scientific Programming with Python

Make a function for each sequence given that returns
an array with the elements in the sequence.  Plot all
the sequences, and find the one that converges fastest
twoard the limit pi.
"""
import numpy as np
import matplotlib.pyplot as plt

N = 20

func_a = np.zeros(N, float)
func_b = np.zeros(N, float)
func_c = np.zeros(N, float)
func_d = np.zeros(N, float)
func_e = np.zeros(N, float)

for n in range(1,N):
	a_n = np.zeros(n, float)
	b_n = np.zeros(n, float)
	c_n = np.zeros(n, float)

	k = 1
	while k <= n:
		a_n[k-1] = ((-1.)**(k+1.))/(2.*k - 1.)
		b_n[k-1] = k**(-2)
		c_n[k-1] = k**(-4)
		k += 1

	func_a[n-1] = 4.*np.sum(a_n)
	func_b[n-1] = np.sqrt(6*np.sum(b_n))
	func_c[n-1] = (90.*np.sum(c_n))**(0.25)

for n in range(1,N):
	d_n = np.zeros(n, float)
	e_n1 = np.zeros(n, float)
	e_n2 = np.zeros(n, float)

	k = 0
	while k < n:
		d_n[k] = ((-1.)**k)/(3.**k*(2.*k + 1))
		e_n1[k] = ((-1.)**k)/(5.**(2.*k + 1) * (2.*k+1))
		e_n2[k] = ((-1.)**k)/(239.**(2.*k + 1) * (2.*k+1))
		k += 1

	func_d[n-1] = (6./np.sqrt(3.))*np.sum(d_n)
	func_e[n-1] = 16.*np.sum(e_n1) - 4.*np.sum(e_n2)

xarr = np.arange(N-1)

plt.plot(xarr,func_a[:-1],linestyle='-',markersize=2,marker='o')
plt.plot(xarr,func_b[:-1],linestyle='-',markersize=2,marker='o')
plt.plot(xarr,func_c[:-1],linestyle='-',markersize=2,marker='o')
plt.plot(xarr,func_d[:-1],linestyle='-',markersize=2,marker='o')
plt.plot(xarr,func_e[:-1],linestyle='-',markersize=2,marker='o')
plt.plot(xarr,xarr*0 + np.pi,linestyle='--',color='k')
plt.show()
