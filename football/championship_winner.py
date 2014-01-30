import numpy as np
import matplotlib.pyplot as plt


tdwn = 7. #touchdown
fldg = 3. #field goal
sfty = 2. #safety

# can run and pass on offense
# defense blocks

teamA_offense_score = [] # 
teamA_defense_score = [] #seattle is 1/30
teamB_offense_score = [] # 
teamB_defense_score = [] #49ers is 4/30  league average for SB winning defense is top 5

Ngames = 16.

QB_SHs = {}
QB_SHs['pass_yrd'] = 3357.
QB_SHs['tds'] = 26
QB_SHs['rating'] = 101.2 #ability for QB to pass for yards and touchdowns vs interceptions and lost yards
QB_SHs['rushing'] = 531
QB_SHs['rushing_td'] = 1

WR_SHs = {} # 4 of them
WR_SHs['GT_catches'] = 64.
WR_SHs['GT_touchdowns'] = 5.
WR_SHs['GT_yards'] = 898.
WR_SHs['GT_games'] = 16.

WR_SHs['SR_catches'] = 15.
WR_SHs['SR_touchdowns'] = 3.
WR_SHs['SR_yards'] = 231.
WR_SHs['SR_games'] = 8.

WR_SHs['rest_rank'] = 6.5 # out of 10

TE_SHs = {}
TE_SHs['games'] = 14.
TE_SHs['catches']= 33.
TE_SHs['yards'] = 387.
TE_SHs['tds'] = 5.

OL_SHs = {} # Offensive line; protecting QB when passing, and RB when running
OL_SHs['sacks_allowed'] = 44
OL_SHs['yards_tot'] = 5424

RB_SHs = {}
RB_SHs['rushing'] = 1257 # Marshawn Lynch
RB_SHs['tds'] = 12

WLrecord_SH = [13,3] # Wins-Losses

kick_SHs = 9 # out of 10

## -------------------

QB_49s = {}
QB_49s['pass_yrd'] = 3197.
QB_49s['tds'] = 21.
QB_49s['rating'] = 91.6
QB_49s['rushing'] = 524.
QB_49s['rushing_td'] = 4

WR_49s = {}
WR_49s['AB_catches'] = 85.
WR_49s['AB_touchdowns'] = 7.
WR_49s['AB_yards'] = 1179.
WR_49s['AB_games'] = 16.

WR_49s['MC_catches'] = 19.
WR_49s['MC_yards'] = 284.
WR_49s['MC_games'] = 1.
WR_49s['MC_touchdowns'] = 5.

WR_49s['rest_rank'] = 4 # out of 10

TE_49s = {}
TE_49s['catches'] = 52.
TE_49s['games'] = 15.
TE_49s['yards'] = 850.
TE_49s['tds'] = 13.

OL_49s = {} # Offensive line; protecting QB when passing, and RB when running
OL_49s['sacks_allowed'] = 39.
OL_49s['yards_tot'] = 5180.

RB_49s = {}
RB_49s['rushing'] = 1128.# Frank Gore
RB_49s['tds'] = 9.

WLrecord_49s = [12,4]

kick_49s = 8. # (out of 10)


## > 0.5 = seahawks
# 'Seahawks (1.0) or 49ers (0.0)? % i' % (np.round(QBrating/4.))
## Compare Quarterbacks:
QBrating = (QB_SHs['pass_yrd']/float(QB_49s['pass_yrd'])) 
QBrating2 = (QB_SHs['tds']/float(QB_49s['tds']))
QBrating3 = (QB_SHs['rushing']/float(QB_49s['rushing']))
#QBrating4 = (QB_SHs['rushing_td']/float(QB_49s['rushing_td'])) 
print '\nQuarterback Comparison'
print QBrating
print QBrating2
print QBrating3
print '\n'


## Compare Wide Receivers
WRrating = (WR_SHs['GT_catches']/WR_SHs['GT_games'] + WR_SHs['SR_catches']/WR_SHs['SR_games'])/(WR_49s['AB_catches']/WR_49s['AB_games'] + WR_49s['MC_catches']/WR_49s['MC_games'])
WRrating2 = (WR_SHs['GT_touchdowns']/WR_SHs['GT_games'] + WR_SHs['SR_touchdowns']/WR_SHs['SR_games'])/(WR_49s['AB_touchdowns']/WR_49s['AB_games'] + WR_49s['MC_touchdowns']/WR_49s['MC_games'])
WRrating3 = (WR_SHs['GT_yards']/WR_SHs['GT_games'] + WR_SHs['SR_yards']/WR_SHs['SR_games'])/(WR_49s['AB_yards']/WR_49s['AB_games'] + WR_49s['MC_yards']/WR_49s['MC_games'])
#WRrating4 = WR_SHs['rest_rank']/WR_49s['rest_rank']

print 'Wide Receiver Comparison'
print WRrating
print WRrating2
print WRrating3
print '\n'


## Compare Tight Ends
TErating = (TE_SHs['catches']/TE_SHs['games'] + TE_SHs['catches']/TE_SHs['games'])/(TE_49s['catches']/TE_49s['games'] + TE_49s['catches']/TE_49s['games'])
TErating2 = (TE_SHs['tds']/TE_SHs['games'] + TE_SHs['tds']/TE_SHs['games'])/(TE_49s['tds']/TE_49s['games'] + TE_49s['tds']/TE_49s['games'])
TErating3 = (TE_SHs['yards']/TE_SHs['games'] + TE_SHs['yards']/TE_SHs['games'])/(TE_49s['yards']/TE_49s['games'] + TE_49s['yards']/TE_49s['games'])
#WRrating4 = WR_SHs['rest_rank']/WR_49s['rest_rank']

print 'Tight Ends Comparison'
print TErating
print TErating2
print TErating3
print '\n'


# Compare Offensive Lines
OLrating = OL_49s['sacks_allowed']/OL_SHs['sacks_allowed']
OLrating2 = OL_SHs['yards_tot']/OL_49s['yards_tot']

print 'Offensive Lines Comparison'
print OLrating
print OLrating2
print '\n'


# Compare Running Backs
RBrating = RB_SHs['rushing']/RB_49s['rushing']
RBrating2 = RB_SHs['tds']/RB_49s['tds']

print 'Running Backs Comparison'
print RBrating
print RBrating2
print '\n'


# Compare Kickers
print 'Kicker Comparison'
KKrating = kick_SHs/kick_49s
print KKrating
print '\n'

Total = np.average((QBrating,QBrating2,QBrating3,WRrating,WRrating2,WRrating3,TErating,TErating2,TErating3,
	OLrating,OLrating2,RBrating,RBrating2,OLrating,OLrating2,RBrating,RBrating2))

print 'Seahawks (> 1.0) or 49ers (< 1.0)? % i' % (Total)
print Total