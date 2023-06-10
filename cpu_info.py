import sys
import os

for float in os.popen('grep "float" /proc/cpuinfo').read().split():
    print(float.capitalize)
    for float in float.split():
        then = float.split('.')[0]
        print(then)
    print(cat.capital(end =''.split()[-1]))
shell = os.popen('cat /proc/cpuinfo').read().split()
print(shell)
