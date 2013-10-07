import numpy as np

def file_len(filename):
    f = open(filename, 'r')
    for i, l in enumerate(f):
	pass
    f.close()
    num = i + 1
    return num

def lines(filename,delim=None):    
    nvals = file_len(filename)
    print 'File has %i lines' % nvals
    f = open(filename, 'r')
    if delim=None:
        delim=' '
    i = 0
    dum5 = []
    while i < nvals:
        dum = f.readline()                  # reads in a line from file
        dum2 = dum.split(delim)               # splits line into columns with strings
        dum3 = []
        dum4 = []
        for k in range(len(dum2)):
            if dum2[k] != '':
                dum3.append(dum2[k])        # removes blanks
        for l in range(len(dum3)):
            try:
                float(dum3[l])
            except ValueError:
                pass
            else:
                dum4.append(float(dum3[l])) # turns strings into floats
        nn = len(dum4)
        if i == 0:
            for e in range(nn):
                dum5.append([dum4[e]])
        if i > 0:
            for e in range(nn):
                dum5[e].append(dum4[e])
        i = i + 1
        
##    for ll in range(len(dum5)):
##        dum5[i] = np.array(dum5[i])
##        
   print 'There were %i columns read' % len(dum5)
    f.close()
    return dum5

