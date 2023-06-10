import sys
import os

for os in sys.path:
    thename = os.split('/')[-1]
    then = thename.split('.')
    list = ["/", then]
    print(list)
