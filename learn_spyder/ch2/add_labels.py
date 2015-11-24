# -*- coding: utf-8 -*-
"""
Created on Wed Apr 15 09:01:46 2015

@author: Nick
"""

# -*- coding: utf-8 -*-
"""
Created on Wed Apr 15 07:41:43 2015

@author: Nick
"""

import csv
from datetime import datetime

fields = ["itemID", "Name", "Description", "Owner", "Price", "Condition", 
"DateRegistered"]

with open("tooldesc2.csv") as td_in:
    rdr = csv.DictReader(td_in, fieldnames=fields)
    items = [item for item in rdr]
    
with open("tooldesc3.csv", "w") as td_out :
    wrt = csv.DictWriter(td_out, fieldnames=fields)
    wrt.writeheader()
    wrt.writerows(items)
