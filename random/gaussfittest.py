import numpy as np
import matplotlib.pyplot as plt
import matplotlib.mlab as mlab
from sklearn.mixture import GMM

x1 = np.random.randn(1*1E4) + np.random.randint(0,np.random.random()*20)
xs1 = np.sort(x1)

x2 = np.random.randn(3*1E4) + np.random.randint(0,np.random.random()*20)
xs2 = np.sort(x2)

x3 = np.random.randn(2*1E4) + np.random.randint(0,np.random.random()*20)

x = np.concatenate([x1,x2,x3])
xs = np.sort(x)

model1 = GMM(3)
model1.fit(x)
alph1 = model1.weights_
mu1 = model1.means_
sig1 = model1.covars_

y1 = mlab.normpdf(xs,mu1[0],sig1[0])
y2 = mlab.normpdf(xs,mu1[1],sig1[1])
y3 = mlab.normpdf(xs,mu1[2],sig1[2])
y4 = alph1[0]*y1 + alph1[1]*y2 + alph1[2]*y3


model2 = GMM(2)
model2.fit(x)
alph2 = model2.weights_
mu2 = model2.means_
sig2 = model2.covars_

w1 = mlab.normpdf(xs,mu2[0],sig2[0])
w2 = mlab.normpdf(xs,mu2[1],sig2[1])
w3 = alph2[0]*w1 + alph2[1]*w2


model3 = GMM(3)
model3.fit(x)
alph3 = model3.weights_
mu3 = model3.means_
sig3 = model3.covars_

r = mlab.normpdf(xs,mu3[0],sig3[0])

plt.figure(figsize=(12,6))
plt.subplot(1,3,1)
plt.hist(x,bins=100,normed=True)
plt.plot(xs,r)

plt.subplot(1,3,2)
plt.hist(x,bins=100,normed=True)
plt.plot(xs,alph2[0]*w1);plt.plot(xs,alph2[1]*w2);plt.plot(xs,w3)

plt.subplot(1,3,3)
plt.hist(x,bins=100,normed=True)
plt.plot(xs,alph1[0]*y1);plt.plot(xs,alph1[1]*y2);plt.plot(xs,alph1[2]*y3);plt.plot(xs,y4)

plt.show()



