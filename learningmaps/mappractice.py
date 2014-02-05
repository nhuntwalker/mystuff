from mpl_toolkits.basemap import Basemap
import numpy as np
import matplotlib.pyplot as plt
import shapefile

m = Basemap(llcrnrlon=-130, urcrnrlon=-60, llcrnrlat=25, urcrnrlat=50, projection='merc', resolution='l')

r = shapefile.Reader(r"./ELSD_2010Census_DP1/ELSD_2010Census_DP1")
geomet = r.shapeRecords() 	#stores the geometry

r2 = shapefile.Reader(r"./SCSD_2010Census_DP1/SCSD_2010Census_DP1")
geomet2 = r2.shapeRecords()

## Rows:
## row 6: Total population
## rows 7 - 24: Different age ranges
##
## row 25: Total male population
## rows 26 - 43: Different age ranges of male population
##
## row 44: Total female population
## rows 45 - 62: Different age ranges of female population
##
## row 63: Median age for both sexes
## row 64: Median age for men
## row 65: Median age for women
##
## row 66: Median age for both sexes above 16 yrs
## row 67: Median age for men
## row 68: Median age for women
##
## row 69: Median age for both sexes above 18 yrs
## row 70: Median age for men
## row 71: Median age for women
##
## row 72: Median age for both sexes above 21 yrs
## row 73: Median age for men
## row 74: Median age for women
##
## row 75: Median age for both sexes above 62 yrs
## row 76: Median age for men
## row 77: Median age for women
##
## row 78: Median age for both sexes above 65 yrs
## row 79: Median age for men
## row 80: Median age for women
##
## row 81: Total population by race
## row 82: Population of one race
## row 83: Population of white people
## row 84: Population of black people
## row 85: Population of natives
## row 86: Population of asians
## rows 87 - 93: Population of each type of asian
## row 94: Population of native hawaiians & pacific islanders
## rows 95 - 98: Population of each type of pacific islander
## row 99: Population of some other race
## row 100: Population of two or more races
## row 101: Whites and Natives
## row 102: Whites and Asians
## row 103: Whites and Blacks
## row 104: Whites and Other races


districtNames = []
districtLats = []
districtLongs = []

for i in range(len(geomet)):
	districtNames.append(geomet[i].record[1])
	districtLats.append(eval(geomet[i].record[4]))
	districtLongs.append(eval(geomet[i].record[5]))


districtNames2 = []
districtLats2 = []
districtLongs2 = []

for i in range(len(geomet2)):
	districtNames2.append(geomet2[i].record[1])
	districtLats2.append(eval(geomet2[i].record[4]))
	districtLongs2.append(eval(geomet2[i].record[5]))
	## Each record after this is the number of each 
	##   row in DP_TableDescriptions.xls

fig = plt.figure()
fig.subplots_adjust(top=0.9,bottom=0.1,left=0.1,right=0.9)

# draw coastlines, countries, and states
m.drawcoastlines()
m.drawstates()
m.drawcountries()
#m.drawcounties()
m.fillcontinents(color='coral',lake_color='aqua')

## draw parallels and meridians.
#m.drawparallels(np.arange(-90.,91.,10.))
#m.drawmeridians(np.arange(-180.,181.,10.))
m.drawmapboundary(fill_color='aqua')
m.plot(districtLongs,districtLats,color='r',marker='.',markersize=2,latlon=True,linestyle='None')
m.plot(districtLongs2,districtLats2,color='b',marker='.',markersize=2,latlon=True,linestyle='None')

plt.show()



