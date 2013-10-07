
yr_arry = range(2002,2013,1)
mon_arry = range(1,13,1)

f = open('get_weather.sh','w')
for yr in yr_arry:
    for mon in mon_arry:
        f.write('wget http://www.wunderground.com/history/airport/KBFI/%i/%i/1/MonthlyHistory.html?format=1 \n' % (yr,mon))
f.close()

