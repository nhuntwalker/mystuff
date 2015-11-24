import sys
from datetime import datetime

time = input("How long did you run? ('MM:SS')\n>>> ")
distance = input("How far did you run? (use quotes)\n>>> ")
units = distance.split(" ")[1]
now_string = datetime.now().strftime("%m/%d/%Y")

minutes = float(time.split(":")[0])
seconds = float(time.split(":")[1])/60

dist = float(distance.split(" ")[0])

if units.startswith("k"):
    dist = dist/1.6

speed = str((minutes + seconds)/dist).split(".")

pace_secs = float("0."+speed[1]) * 60
if pace_secs < 10:
    pace_secs = "0" + str(pace_secs)
else:
    pace_secs = "%.2f" % (pace_secs)

speed[1] = pace_secs
speed = ":".join(speed)

outstr = now_string + "   " + time + "   %.1f mi   " + speed
print outstr % (dist)
