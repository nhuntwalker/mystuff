import numpy as np 
import matplotlib.pyplot as plt 
from gatspy.periodic import LombScargle

z = np.linspace(0, 20, 1000)
W = 500

# Normal L-S periodogram
def davies_z(z, W):
    return np.exp(-z) + W*np.exp(-z)*np.sqrt(z) # strong spectral leakage (Davies Bound)

def alias_free_z(z, W):
    return 1 - (1 - np.exp(-z))*np.exp(-W*np.exp(-z)*np.sqrt(z)) # alias free

fig = plt.figure(figsize=(6,3))
plt.plot(z, davies_z(z, 50), color="b", linestyle="--")
plt.plot(z, alias_free_z(z, 50), color="b")

plt.plot(z, davies_z(z, 500), color="r", linestyle="--")
plt.plot(z, alias_free_z(z, 500), color="r")

plt.plot(z, davies_z(z, 5000), color="g", linestyle="--")
plt.plot(z, alias_free_z(z, 5000), color="g")

plt.yscale("log")
plt.ylim(1E-4, 1)
plt.grid()
plt.show()

# Modified L-S periodogram, Z1
def davies_z1(z, W):
    N = 100
    Psingle = 1 - (1 - 2*z /(N - 1)) ** (0.5*(N - 3))
    gammaH = np.sqrt(2./(N-1))*gamma(0.5*(N-1))/gamma(0.5*(N-2))
    tau = gammaH * W * (1-2*z/(N-1)) ** (0.5*(N-4)) * np.sqrt(z)
    y0 = 1 - Psingle + tau # Davies Bound
    return y0

def alias_free_z1(z, W):
    N = 100
    Psingle = 1 - (1 - 2*z /(N - 1)) ** (0.5*(N - 3))
    gammaH = np.sqrt(2./(N-1))*gamma(0.5*(N-1))/gamma(0.5*(N-2))
    tau = gammaH * W * (1-2*z/(N-1)) ** (0.5*(N-4)) * np.sqrt(z)
    y1 =  1 - Psingle*np.exp(-tau) # alias free
    return y1

fig = plt.figure(figsize=(6,3))
plt.plot(z, davies_z1(z, 50), color="b", linestyle="--")
plt.plot(z, alias_free_z1(z, 50), color="b")

plt.plot(z, davies_z1(z, 500), color="r", linestyle="--")
plt.plot(z, alias_free_z1(z, 500), color="r")

plt.plot(z, davies_z1(z, 5000), color="g", linestyle="--")
plt.plot(z, alias_free_z1(z, 5000), color="g")
plt.yscale("log")
plt.ylim(1E-4, 1)
plt.grid()
plt.show()


## Do the Monte Carlo simulations to generate data and see if FAPs match analytic expressions
# have white noise
# generate periodogram for some range of frequencies, for some length of time
# --- want to find the distribution of Z of the best frequency
# --- distribution of z-values approximates the probability distribution of getting a z value
# --- 1 minus the above is an estimate of FAP(z)
