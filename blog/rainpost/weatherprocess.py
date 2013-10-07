import numpy as np
import matplotlib.pyplot as plt
import readall as read
import astroML as astr
import os
from astroML.stats import binned_statistic_2d

citylow = ['seattle','newyork','losangels']
cityhi = ['Seattle','New York City','Los Angeles']
for i in range(len(citylow)):
    print 'Starting %s' % cityhi[i]
    f1 = 'monthdata/%s/MonthlyHistory.html?format=1' % citylow[i]
    columns,header = read.withcsv(f1,',',header='True',cols='True')
    print header
    date,Tmax,Tmean,Tmin,DewMax = columns[0:5]
    DewMean,DewMin,HumidMax,HumidMean,HumidMin = columns[5:10]
    PressMax,PressMean,PressMin,VisMax,VisMean = columns[10:15]
    VisMin,WindMax,WindMean,GustMax,rain = columns[15:20]
    clouds,event,WindDir = columns[20:]

    nfiles = range(1,131)
    for n in nfiles:
        f2 = 'monthdata/%s/MonthlyHistory.html?format=1.%i' % (citylow[i],n)
        columns,header = read.withcsv(f2,',',header='True',showlines='False')
        j = len(columns[0])
        for k in range(j):
            date.append(columns[0][k]),Tmax.append(columns[1][k]),Tmean.append(columns[2][k]),Tmin.append(columns[3][k]),DewMax.append(columns[4][k])
            DewMean.append(columns[5][k]),DewMin.append(columns[6][k]),HumidMax.append(columns[7][k]),HumidMean.append(columns[8][k]),HumidMin.append(columns[9][k])
            PressMax.append(columns[10][k]),PressMean.append(columns[11][k]),PressMin.append(columns[12][k]),VisMax.append(columns[13][k]),VisMean.append(columns[14][k])
            VisMin.append(columns[15][k]),WindMax.append(columns[16][k]),WindMean.append(columns[17][k]),GustMax.append(columns[18][k]),rain.append(columns[19][k])
            clouds.append(columns[20][k]),event.append(columns[21][k]),WindDir.append(columns[22][k])


    ## Now to do something special with the date.  I want year-month-day out, so...
    yr,mon,dy = [],[],[]
    for d in range(len(date)):
        dum = date[d].split('-')
        yr.append(eval(dum[0])),mon.append(eval(dum[1])),dy.append(eval(dum[2]))


    yr,mon,dy = np.array(yr),np.array(mon),np.array(dy)
    Tmax,Tmean,Tmin = np.array([eval(e) for e in Tmax]),np.array([eval(e) for e in Tmean]),np.array([eval(e) for e in Tmin])
    DewMax,DewMean,DewMin = np.array([eval(e) for e in DewMax]),np.array([eval(e) for e in DewMean]),np.array([eval(e) for e in DewMin])
    HumidMax,HumidMean,HumidMin = np.array([eval(e) for e in HumidMax]),np.array([eval(e) for e in HumidMean]),np.array([eval(e) for e in HumidMin])
    PressMax,PressMean,PressMin = np.array([eval(e) for e in PressMax]),np.array([eval(e) for e in PressMean]),np.array([eval(e) for e in PressMin])
    clouds = np.array([float(eval(e)) for e in clouds])
    rain = np.array(rain)
    if len(np.where(rain == 'T')[0]) != 0:
        rain[np.where(rain == 'T')] = '0'
        rain = np.array([eval(j) for j in rain])
    else:
        rain = np.array([eval(j) for j in rain])
##    rain = np.array([eval(j) for j in rain])
    #VisMax,VisMean,VisMin = np.array([eval(e) for e in VisMax]),np.array([eval(e) for e in VisMean]),np.array([eval(e) for e in VisMin])
    #WindMax,WindMean = np.array([eval(e) for e in WindMax]),np.array([eval(e) for e in WindMean])

    year0 = np.where(yr == 2002)
    clouds = 100.*clouds/8.0  ## To turn into % cloud cover

    allyears = range(min(yr),max(yr)+1)
    months = range(1,13)

    ## Indices according to year
    yr0,yr1,yr2,yr3,yr4 = np.where(yr == 2002),np.where(yr == 2003),np.where(yr == 2004),np.where(yr == 2005),np.where(yr == 2006)
    yr5,yr6,yr7,yr8,yr9,yr10 = np.where(yr == 2007),np.where(yr == 2008),np.where(yr == 2009),np.where(yr == 2010),np.where(yr == 2011),np.where(yr == 2012)

    print 'Cumulative Rain in %s over years' % cityhi[i]
    print sum(rain[yr0]),sum(rain[yr1]),sum(rain[yr2]),sum(rain[yr3]),sum(rain[yr4])
    print sum(rain[yr5]),sum(rain[yr6]),sum(rain[yr7]),sum(rain[yr8]),sum(rain[yr9]),sum(rain[yr10])
    print 'Average Cloud Cover in %s over years' % cityhi[i]
    print np.average(clouds[yr0]),np.average(clouds[yr1]),np.average(clouds[yr2]),np.average(clouds[yr3]),np.average(clouds[yr4]),
    print np.average(clouds[yr5]),np.average(clouds[yr6]),np.average(clouds[yr7]),np.average(clouds[yr8]),np.average(clouds[yr9]),np.average(clouds[yr10]),
##    ## ==========================================================================================================================================
##    ## Plotting Time
##    ## ==========================================================================================================================================
##    fig = plt.figure(figsize=(16,6))
##    fig.suptitle('%s' % cityhi[i], fontsize=15)
##    ## mon, year, rain; x,y,z color plot averaged over months
##    mobin = np.arange(min(mon)-0.5,max(mon)+1.5,1.0)
##    yrbin = np.arange(min(yr)-0.5,max(yr)+1.5,1.0)
##    binxy = (mobin,yrbin)  ## x and y bins
##    rain_mean2, xed, yed = binned_statistic_2d(mon, yr, rain, 'sum', bins=binxy)
##    cmap = plt.cm.Blues
##    cmap.set_bad('w',1.)
##    plt.subplot(131)
##    plt.imshow(rain_mean2.T, origin='lower',extent=[xed[0],xed[-1],yed[0],yed[-1]],aspect='auto',interpolation='nearest',cmap=cmap,vmin=0,vmax=13)
##    cb = plt.colorbar(orientation='horizontal')
##    cb.set_label(r'Inches')
##    plt.xlim(0.5,12.5)
##    lin1x = [4.5,4.5]
##    lin1y = [2000,2050]
##    lin2x = [9.5,9.5]
##    monthnames = 'Jan','Feb','Mar','Apr','May','Jun','Jul','Aug','Sep','Oct','Nov','Dec'
##    plt.xticks(range(1,13), monthnames, rotation=45)
##    plt.yticks(rotation=45)
##    plt.ylim(2001.5,2012.5)
##    plt.ylabel('Year')
##    plt.title('Precipitation (Inches)')
##    plt.plot(lin1x,lin1y, ls='--', c = 'k')
##    plt.plot(lin2x,lin1y, ls='--', c='k')
##    #plt.savefig('rainfall_10yrs_monthly.pdf')
##    ##plt.show()
##
##    ## mon, year, cloud cover; x,y,z color plot averaged over months
##    ## --Note that "cloudy" is when 7/8ths of the sky is covered
##    mobin = np.arange(min(mon)-0.5,max(mon)+1.5,1.0)
##    yrbin = np.arange(min(yr)-0.5,max(yr)+1.5,1.0)
##    binxy = (mobin,yrbin)  ## x and y bins
##    cloud_mean, xed, yed = binned_statistic_2d(mon, yr, clouds, 'mean', bins=binxy)
##    cmap = plt.cm.Greys
##    cmap.set_bad('w',0.)
##    #fig = plt.figure(figsize=(8,4))
##    plt.subplot(132)
##    plt.imshow(cloud_mean.T, origin='lower',extent=[xed[0],xed[-1],yed[0],yed[-1]],aspect='auto',interpolation='nearest',cmap=cmap,vmin=0,vmax=100)
##    cb = plt.colorbar(orientation='horizontal')
##    cb.set_label(r'% clouds')
##    plt.xlim(0.5,12.5)
##    lin1x = [4.5,4.5]
##    lin1y = [2000,2050]
##    lin2x = [9.5,9.5]
##    monthnames = 'Jan','Feb','Mar','Apr','May','Jun','Jul','Aug','Sep','Oct','Nov','Dec'
##    plt.xticks(range(1,13), monthnames, rotation=45)
##    plt.yticks(rotation=45)
##    plt.ylim(2001.5,2012.5)
##    #plt.ylabel('Year')
##    middlec = np.median(clouds)
##    #plt.title('Total Percent Cloud Cover in Seattle; Decadal Median = %.2f prct' % middlec)
##    plt.title('Cloud Cover; Decadal Median = %.2f %%' % middlec)
##    #plt.savefig('cloudcover_10yrs_monthly.pdf')
##    ##plt.show()
##
##    ## mon, year, HumidMean; x,y,z color plot averaged over months
##    plt.subplot(133)
##    mobin = np.arange(min(mon)-0.5,max(mon)+1.5,1.0)
##    yrbin = np.arange(min(yr)-0.5,max(yr)+1.5,1.0)
##    binxy = (mobin,yrbin)  ## x and y bins
##    humid_mean, xed, yed = binned_statistic_2d(mon, yr, HumidMean, 'mean', bins=binxy)
##    cmap1 = plt.cm.Reds
##    cmap1.set_bad('k',0.)
##    #fig = plt.figure(figsize=(8,4))
##    plt.imshow(humid_mean.T, origin='lower',extent=[xed[0],xed[-1],yed[0],yed[-1]],aspect='auto',interpolation='nearest',cmap=cmap1,vmin=0,vmax=100)
##    cb = plt.colorbar(orientation='horizontal')
##    cb.set_label(r'% humidity')
##    plt.xlim(0.5,12.5)
##    monthnames = 'Jan','Feb','Mar','Apr','May','Jun','Jul','Aug','Sep','Oct','Nov','Dec'
##    plt.xticks(range(1,13), monthnames, rotation=45)
##    plt.yticks(rotation=45)
##    plt.ylim(2001.5,2012.5)
##    #plt.ylabel('Year')
##    middlec = np.median(HumidMean)
##    plt.title('Humidity; Decadal Median = %.2f %%' % middlec)
##    #plt.title('Total Percent Humidity in Seattle; Decadal Median = %.2f prct' % middlec)
##    #plt.savefig('humidity_10yrs_monthly.pdf')
##    plt.savefig('%sweather_10yrs_monthly.png' % citylow[i])
##    plt.show()
##    print 'Plotting For %s Done' % cityhi[i]
























#### This is for plotting a line graph of
####    rainfall over time
##date = np.array(date)
##day = np.array(range(1,len(date)+1))  ## This is just to count days
##day0 = day[year0]                     ## for year 2002
##rain0 = rain[year0]
##plt.plot(day0,rain0,'bx',ls = '-')
##plt.xlabel('Day of the Year')
##plt.ylabel('Rain (in)')
##plt.xlim(0,day0)
##plt.ylim(min(rain0)-0.1*min(rain0),max(rain0)+0.1*max(rain0))
##plt.show()


