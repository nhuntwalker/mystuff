import os
import pylab
import json
from pandas import DataFrame, Series
import numpy as np

os.chdir("/Users/Nick/Documents/my_python/mystuff/dataanalysis/data_library/usa_gov/")
inputs = "usagov_bitly_data2012-03-16-1331923249"
records = [json.loads(line) for line in open(inputs)]

# time_zones = [rec['tz'] for rec in records if 'tz' in rec]

# def get_counts(sequence):
# 	counts = {}
# 	for x in sequence:
# 		if x in counts:
# 			counts[x] += 1
# 		else:
# 			counts[x] = 1
# 	return counts

# counts = get_counts(time_zones)
# print counts['America/New_York']

frame = DataFrame(records)
clean_tz = frame['tz'].fillna('Missing')
clean_tz[clean_tz == ''] = "Unknown"
tz_counts = clean_tz.value_counts()

tz_counts[:10].plot(kind='barh', rot=0)