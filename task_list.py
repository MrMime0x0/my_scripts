import os
os.system('ps aux')
print(os.popen('ps aux').read().split('\n')[1])
