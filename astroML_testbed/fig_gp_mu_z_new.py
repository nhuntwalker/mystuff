"""
Cosmology Regression Example
----------------------------
Figure 8.11

A Gaussian process regression analysis of the simulated supernova sample used
in figure 8.2. This uses a squared-exponential covariance model, with bandwidth
learned through cross-validation.
"""
# Author: Jake VanderPlas
# License: BSD
#   The figure produced by this code is published in the textbook
#   "Statistics, Data Mining, and Machine Learning in Astronomy" (2013)
#   For more information, see http://astroML.github.com
#   To report a bug or issue, use the following forum:
#    https://groups.google.com/forum/#!forum/astroml-general

from __future__ import print_function, division

import numpy as np
from matplotlib import pyplot as plt

from sklearn.gaussian_process import GaussianProcess
import george
from george.kernels import ExpSquaredKernel

# from astroML.cosmology import Cosmology
from astropy.cosmology import FlatLambdaCDM as Cosmology
from astroML.datasets import generate_mu_z

#----------------------------------------------------------------------
# This function adjusts matplotlib settings for a uniform feel in the textbook.
# Note that with usetex=True, fonts are rendered with LaTeX.  This may
# result in an error if LaTeX is not installed on your system.  In that case,
# you can set usetex to False.
from astroML.plotting import setup_text_plots
setup_text_plots(fontsize=8, usetex=True)

#------------------------------------------------------------
# Generate data
# z_sample, mu_sample, dmu = generate_mu_z(100, random_state=0)
z_sample, mu_sample, dmu = generate_mu_z(100, random_state=0, Om0=0.27, H0=71)

# cosmo = Cosmology()
cosmo = Cosmology(Om0=0.27, H0=71)
z = np.linspace(0.01, 2, 1000)
# mu_true = np.asarray([cosmo.mu(zi) for zi in z])
mu_true = np.asarray(cosmo.distmod(z).value)

#------------------------------------------------------------
# fit the data
# Mesh the input space for evaluations of the real function,
# the prediction and its MSE
z_fit = np.linspace(0, 2, 1000)

#------------------------------------------------------------
# using scikit-learn
gp_sk = GaussianProcess(corr='squared_exponential', theta0=1e-1,
                     thetaL=1e-2, thetaU=1,
                     normalize=False,
                     nugget=(dmu / mu_sample) ** 2,
                     random_start=1)
gp_sk.fit(z_sample[:, None], mu_sample)
y_pred_sk, MSE_sk = gp_sk.predict(z_fit[:, None], eval_MSE=True)
sigma_sk = np.sqrt(MSE_sk)
print("theta:", gp_sk.theta_)

#------------------------------------------------------------
# using george
gp = george.GP(ExpSquaredKernel(0.5/1e-2))
gp.compute(z_sample, (dmu/mu_sample)**2)
y_pred, MSE = gp.predict(mu_sample, z_fit)
sigma = np.sqrt(np.diag(MSE))

#------------------------------------------------------------
# Plot the gaussian process
#  gaussian process allows computation of the error at each point
#  so we will show this as a shaded region
fig = plt.figure(figsize=(5, 5))
fig.subplots_adjust(left=0.1, right=0.95, bottom=0.1, top=0.95, hspace=0)
ax = fig.add_subplot(211)

ax.plot(z, mu_true, '--k')
ax.errorbar(z_sample, mu_sample, dmu, fmt='.k', ecolor='gray', markersize=6)
ax.plot(z_fit, y_pred_sk, '-k')
ax.fill_between(z_fit, y_pred_sk - 1.96 * sigma_sk, y_pred_sk + 1.96 * sigma_sk,
                alpha=0.2, color='b', label='95% confidence interval')

ax.text(0.9, 0.1, "Gaussian Process from sklearn", transform=ax.transAxes, horizontalalignment="right")
# ax.set_xlabel('$z$')
ax.set_ylabel(r'$\mu$')

ax.set_xlim(0, 2)
ax.set_xticklabels([])
ax.set_ylim(36, 48)

ax = fig.add_subplot(212)

ax.plot(z, mu_true, '--k')
ax.errorbar(z_sample, mu_sample, dmu, fmt='.k', ecolor='gray', markersize=6)
ax.plot(z_fit, y_pred, '-k')
ax.fill_between(z_fit, y_pred - 1.96 * sigma, y_pred + 1.96 * sigma,
                alpha=0.2, color='r', label='95% confidence interval')
# ax.fill_between(z_fit, y_pred - 4000 * sigma, y_pred + 4000 * sigma,
#                 alpha=0.2, color='r', label='95% confidence interval')

ax.text(0.9, 0.1, "Gaussian Process from george", transform=ax.transAxes, horizontalalignment="right")
ax.set_xlabel('$z$')
ax.set_ylabel(r'$\mu$')

ax.set_xlim(0, 2)
ax.set_ylim(36, 48)

# plt.savefig("/Users/Nick/Documents/my_python/mystuff/astroML_testbed/fig_gp_mu_z_proper.pdf")
plt.show()
