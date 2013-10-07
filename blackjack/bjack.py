import random as rd
import numpy as np
from Tkinter import *
root = Tk()

hearts = ['aceH','twoH','thrH','furH','fivH','sixH','sevH','eghH','ninH','tenH','jakH','qenH','kngH']
clubs = ['aceC','twoC','thrC','furC','fivC','sixC','sevC','eghC','ninC','tenC','jakC','qenC','kngC']
diamonds = ['aceD','twoD','thrD','furD','fivD','sixD','sevD','eghD','ninD','tenD','jakD','qenD','kngD']
spades = ['aceS','twoS','thrS','furS','fivS','sixS','sevS','eghS','ninS','tenS','jakS','qenS','kngS']
deck = np.concatenate((hearts,clubs,diamonds,spades))

rd.shuffle(deck)
deck = list(deck)

def hand_eval(allcards):
    handval = []
    for crd in allcards:
        if crd.startswith('ace') == True:
            handval.append(11)
        elif crd.startswith('two') == True:
            handval.append(2)
        elif crd.startswith('thr') == True:
            handval.append(3)
        elif crd.startswith('fur') == True:
            handval.append(4)
        elif crd.startswith('fiv') == True:
            handval.append(5)
        elif crd.startswith('six') == True:
            handval.append(6)
        elif crd.startswith('sev') == True:
            handval.append(7)
        elif crd.startswith('egh') == True:
            handval.append(8)
        elif crd.startswith('nin') == True:
            handval.append(9)
        elif crd.startswith('ten') == True:
            handval.append(10)
        elif crd.startswith('jak') == True:
            handval.append(10)
        elif crd.startswith('qen') == True:
            handval.append(10)
        elif crd.startswith('kng') == True:
            handval.append(10)
    return sum(handval)

    
plyr1,comp = [],[]
plyr1.append(deck.pop())
comp.append(deck.pop())

plyr1.append(deck.pop())
comp.append(deck.pop())

def hit():
    plyr1.append(deck.pop())
    hand_label.configure(text='%g' % hand_eval(plyr1))

plyrhit = Button(root, text='Hit', command=hit)
plyrhit.pack(side='left', padx=20)

hand_label = Label(root, width=8)
hand_label.pack(side='left')
root.mainloop()

print plyr1
print hand_eval(plyr1)
print 'Dealer is showing', comp[0], hand_eval([comp[0]])

for i in range(100):
    nextmove = raw_input('Hit or Stand?\n')
    if nextmove.lower() == 'hit':
        plyr1.append(deck.pop())
        if hand_eval(plyr1) > 21:
            print plyr1
            print "You've hit %i!! Bust!" % hand_eval(plyr1)
            break
        print hand_eval(plyr1)
    elif nextmove.lower() == 'stand':
        print plyr1
        print hand_eval(plyr1)
        break

print 'Dealer has:', comp, hand_eval(comp)
while hand_eval(comp) < 17 and hand_eval(plyr1) <22:
    comp.append(deck.pop())
    print 'Dealer has:', comp, hand_eval(comp)

if (hand_eval(plyr1) > hand_eval(comp) and hand_eval(plyr1) < 22) or hand_eval(comp) > 21:
    print 'You Win!'
elif hand_eval(comp) > hand_eval(plyr1) or hand_eval(plyr1) > 21:
    print 'You lose.'
elif hand_eval(comp) == hand_eval(plyr1):
    print 'Same hands.  Push.'

