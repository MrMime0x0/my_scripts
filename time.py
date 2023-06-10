import sys
import os

time = getsystemtime = lambda: os.times()[4]
for time in range(0, 10):
    getsystemtime()
    time = getsystemtime()
    sys.executable = "uptime"
    print(time)
