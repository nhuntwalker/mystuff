#import pyfits
import numpy as np
import matplotlib.pyplot as plt
import readall as r
from intersect import inters

filesred = ['specfiles/hilt600_26r.txt','specfiles/st1_28r.txt','specfiles/st3_32r.txt','specfiles/st6_29r.txt','specfiles/st7_30r.txt','specfiles/xxcam_25r.txt','specfiles/xxcam_24r.txt']
filesblu = ['specfiles/hilt600_26b.txt','specfiles/st1_28b.txt','specfiles/st3_32b.txt','specfiles/st6_29b.txt','specfiles/st7_30b.txt','specfiles/xxcam_25b.txt','specfiles/xxcam_24b.txt']
plttit = ['HILT 600','Unknwn 1','Unknwn 3','Unknwn 6','Unknwn 7','XX Cam']
fnames = ['hilt600.pdf','st1_28spec.pdf','st3_32spec.pdf','st6_29spec.pdf','st7_30spec.pdf','xxcam_24spec.pdf']

i = 5
#for i in range(len(fnames)):
datared = r.withcsv(filesred[i])
wave_r = np.array(datared[0]); band_r = np.array(datared[2]); flux_r = np.array(datared[3])
wave_r = wave_r.astype(float); flux_r = flux_r.astype(float)
spec1_r = np.where(band_r=='1.')
spec2_r = np.where(band_r=='2.')
wv_r = wave_r[spec1_r]; fl_r = flux_r[spec1_r]
badlo_r = np.where(wv_r > 6925)
badhi_r = np.where(wv_r < 6945)
bad_r = inters([badlo_r,badhi_r])
wv_r,fl_r = np.delete(wv_r,bad_r),np.delete(fl_r,bad_r)

datablue = r.withcsv(filesblu[i])
wave_b,band_b,flux_b = np.array(datablue[0]),np.array(datablue[2]),np.array(datablue[3])
wave_b,flux_b = wave_b.astype(float),flux_b.astype(float)
spec1_b = np.where(band_b=='1.')
wv_b,fl_b = wave_b[spec1_b],flux_b[spec1_b]

hbalmer = np.array([656.3,486.1,434.1,410.2,397.0,388.9,383.5,364.6])
hbalmer = hbalmer*10
carbon = [3880,4056,4217,4380,4581,4640,4738,4867,4906,4977,5165,5635,6059,6100,6122,6168,6191]
blanks1 = np.zeros(len(carbon))
blanks2 = np.zeros(len(hbalmer))
bluegood = np.where(wv_b < 5400)
redgood = np.where(wv_r > 5400)

plt.figure(figsize=(7,5))
plt.plot(wv_r[redgood],fl_r[redgood],c='r')
plt.plot(wv_b[bluegood],fl_b[bluegood],c='b')
##plt.scatter(hbalmer,blanks2+max(fl_b),c='k',marker='v')
#plt.scatter(carbon,blanks1+max(fl_b),c='k',marker='v')
plt.xlabel('Angstroms [$\AA$]');plt.ylabel('Flux [ergs cm$^{-2}$ s$^{-1}$ $\AA^{-1}$]')
#    plt.xlim(min(wv_b),max(wv_r));plt.ylim(min(fl_r),max(fl_b));plt.ylim=(min(fl_r),max(fl_b))
plt.xlim(4270,4900)#;plt.ylim(0.2E-12,0.4E-12)
#plt.xticks(np.arange(40,96,10.)*100)
plt.title(plttit[i])
#plt.savefig(fnames[i])
plt.show()


##files = ['hilt600_26r.msdisp.fits','st3_32r.mscal.fits','st4_27r.mscal.fits','st5_31r.mscal.fits','st6_29r.mscal.fits','st7_30r.mscal.fits','st8_33r.mscal.fits','xxcam_24r.mscal.fits','xxcam_25r.mscal.fits']
##comps = ['compcam.fits','compst3.fits','compst4.fits','compst5.fits','compst6.fits','compst7.fits','compst8.fits','compcam.fits','compcam25.fits']
##data = pyfits.open(files[0])
##dat = data[0]


##plt.plot(dat.data[1][0])
##plt.plot(dat.data[1][0]-dat.data[0][0])
##plt.plot(dat.data[0][0]-dat.data[1][0])  ## this is the background-subtracted spectrum
##plt.show()
