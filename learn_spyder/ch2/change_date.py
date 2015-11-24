# -*- coding: utf-8 -*-
"""
Created on Wed Apr 15 07:41:43 2015

@author: Nick
"""

import csv
from datetime import datetime

def convertDate(item):
    theDate = item[-1]
    dateObj = datetime.strptime(theDate, "%Y-%m-%d")
    dateStr = datetime.strftime(dateObj, "%m/%d/%Y")
    item[-1] = dateStr
    return item

with open("tooldesc.csv") as td:
    rdr = csv.reader(td)
    items = list(rdr)
    
items = [convertDate(item) for item in items]
with open("tooldesc2.csv", "w") as td :
    wrt = csv.writer(td)
    for item in items:
        wrt.writerow(item)
        
