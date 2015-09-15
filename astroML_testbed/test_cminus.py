import numpy as np
import matplotlib.pyplot as plt
from scipy import stats
from astroML.lumfunc import _sorted_interpolate, Cminus, binned_Cminus, bootstrap_Cminus

#------------------------------------------------------
# setup the plotting environment
from astroML.plotting import setup_text_plots
setup_text_plots(fontsize=8, usetex=True)

#------------------------------------------------------
# define and sample our distributions
N = 10000
np.random.seed(42)

# Define the input distributions for x and y
x_pdf = stats.truncnorm(-2, 1, 0.66666, 0.33333)
y_pdf = stats.truncnorm(-1, 2, 0.33333, 0.33333)

x = x_pdf.rvs(N)
y = y_pdf.rvs(N)

# Define the trunctation: we'll design this to be symmetric
# so that xmax(y) = max_func(y)
# and ymax(x) = max_func(x)
max_func = lambda t: 1. / (0.5 + t) - 0.5

xmax = max_func(y)
xmax[xmax > 1] = 1 #cutoff at x=1

ymax = max_func(x)
ymax[ymax > 1] = 1 #cutoff at y=1

# truncate the data
flag = (x < xmax) & (y < ymax)
x = x[flag]
y = y[flag]
xmax = xmax[flag]
ymax = ymax[flag]

xbins = np.linspace(0, 1, 21)
ybins = np.linspace(0, 1, 21)

#--------------------------------------------------
# compute the C-minus distributions step by step
Nx, Ny, cuml_x, cuml_y = Cminus(x, y, xmax, ymax)
# simple linear interpolation using a binary search
# interpolate the cumulative distributions
x_sort = np.sort(x)
y_sort = np.sort(y)

Ix_edges = _sorted_interpolate(x_sort, cuml_x, xbins)
Iy_edges = _sorted_interpolate(y_sort, cuml_y, ybins)

if xbins[0] < x_sort[0]:
    Ix_edges[0] = cuml_x[0]
if xbins[-1] > x_sort[-1]:
    Ix_edges[-1] = cuml_x[-1]

if ybins[0] < y_sort[0]:
    Iy_edges[0] = cuml_y[0]
if ybins[-1] > y_sort[-1]:
    Iy_edges[-1] = cuml_y[-1]

x_dist = np.diff(Ix_edges) / np.diff(xbins)
y_dist = np.diff(Iy_edges) / np.diff(ybins)

x_dist /= len(x)
y_dist /= len(y)




