import numpy as np
import matplotlib.pyplot as plt
from scipy.stats import norm, multivariate_normal

xgrid, ygrid = np.mgrid[-10:10:0.1, -10:10:0.1]
coords = np.dstack((xgrid, ygrid))