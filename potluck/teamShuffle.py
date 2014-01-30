import os
import numpy as np

os.chdir('/Users/Nick/Documents/my_python/mystuff/potluck/')

infile = 'guests.txt'
people = np.genfromtxt(infile, dtype='S20')
#np.random.seed(0)
np.random.shuffle(people)

npeople = float(len(people))
nteams = int(raw_input('How Many Teams Are Playing? (2-4):\n'))

teams = []
for i in range(int(nteams)):
	teams.append([])
	teams[i] = list(people[npeople/nteams*i:npeople/nteams*(i+1)])
	if i == nteams-1:
		teams[i] = list(people[npeople/nteams*i:])


teamsmax = []
for i in range(len(teams)):
	teamsmax.append(len(teams[i]))

for t in teams:
	if len(t) != max(teamsmax):
		t.append(' ')
	# print '%s\n' % t

teams = np.array(teams).T

outfile = open('teams.rtf','w')
outfile.write('{\\rtf1\\ansi\\ansicpg1252\\cocoartf1265\n')
outfile.write('{\\fonttbl\\f0\\fswiss\\fcharset0 Helvetica;}\n')
outfile.write('{\\colortbl;\\red255\\green255\\blue255;}\n')
outfile.write('\\margl1440\\margr1440\\vieww25200\\viewh20000\\viewkind0\n')
outfile.write('\\pard')
for i in range(nteams):
	outfile.write('\\tx%i' % ((i+1)*6480))

outfile.write('\\pardirnatural\n')

outfile.write('\n')
outfile.write('\\f0\\fs128 \\cf0 ')	# The font size is controlled by "fs"
#outfile.write('\\f0\\fs128 \\cf0 ')	# The font size is controlled by "fs"
									# The number is 2x the actual font size
for i in range(nteams):
	if i == nteams-1:
		outfile.write('Team %i\\\n' % (i+1))
	else:
		outfile.write('Team %i\t' % (i+1))

for i in range(len(teams)):
	for j in range(len(teams[i])):
		if j == len(teams[i])-1:
			outfile.write('%s\\\n' % teams[i][j])
		else:
			outfile.write('%s\t' % teams[i][j])
outfile.write('}')

outfile.close()
