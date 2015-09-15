import numpy as np
import matplotlib.pyplot as plt
from gatspy.periodic import LombScargle
import sys

N_trials = 10000 # 10,000 
N_pts = 1000

# time array
t = np.linspace(0, 100, N_pts)

fnum = eval(sys.argv[1])

W = [50, 500]
scores = np.zeros((N_trials, len(W)))

for ii in range(N_trials):

    for jj in range(len(W)):
        # maximum frequency/min period
        fmax = W[jj]/t.max()
        
        # "data" array
        y = np.random.normal(0, 1.0, t.size)

        ls = LombScargle().fit(t, y, 1.0)
        ls.optimizer.quiet = True
        ls.optimizer.period_range = (1/fmax, t[-1])

        chisq_0 = np.var(y)
        scores[ii, jj] = ls.score(ls.best_period) * chisq_0 * 0.5 * (N_pts-1)

fout = open("output{0}.dat".format(fnum), "w")

for ii in range(N_trials):
    fout.write("{0},{1}\n".format(scores[ii,0], scores[ii,1]))

fout.close()


# data = data[:100000]
# data = scores * (N_pts-1)
qw1 = np.percentile(data.T[0], [75,25])
qw2 = np.percentile(data.T[1], [75,25])
qw1 = qw1[0] - qw1[1]
qw2 = qw2[0] - qw2[1]
bw1 = 2*qw1 / (1E5)**(1./3)
bw2 = 2*qw2 / (1E5)**(1./3)
# bw1 = 2*qw1 / (5E2)**(1./3)
# bw2 = 2*qw2 / (5E2)**(1./3)

H1, bins1 = np.histogram(data.T[0], bins=np.arange(0, max(data.T[0]) + bw1, bw1))
H2, bins2 = np.histogram(data.T[1], bins=np.arange(0, max(data.T[1]) + bw2, bw2))

H1 = np.cumsum(H1)
H2 = np.cumsum(H2)

fig = plt.figure(figsize=(6,4))
fig.subplots_adjust(bottom=0.15)
plt.title("$N = 1000$ time steps, evenly-spaced, $10^5$ runs")
# plt.title("$N = 1000$ time steps, evenly-spaced, $5x10^2$ runs")
plt.step(bins1[:-1], 1 - H1/float(max(H1)), color='b', label="f$_{max}T = 50$")
plt.step(bins2[:-1], 1 - H2/float(max(H2)), color='r', label="f$_{max}T = 500$")
plt.xlabel("max Z")
plt.ylabel("N")
plt.legend(loc="best")
plt.ylim(1E-4,1)
plt.yscale("log")
plt.minorticks_on()
plt.grid()

plt.show()
