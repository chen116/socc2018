from os import listdir
from os.path import isfile, join
onlyfiles = [f for f in listdir('./') if isfile(join('./', f))]
# print(onlyfiles)

files = [ f for f in onlyfiles if "mult_" in f]
print(files)




import matplotlib.pyplot as plt
import matplotlib.animation as animation
from matplotlib.widgets import Cursor
from matplotlib.font_manager import FontProperties
from matplotlib.widgets import CheckButtons

import time
for f in files:
    fig = plt.figure(figsize=(10, 7))
    ax1 = fig.add_subplot(1,1,1)

    x = []
    cyc = []
    pullData = open(f,"r").read()
    dataArray = pullData.split('\n')
    for eachLine in dataArray:
        if len(eachLine)>1:
            line = eachLine.split()
            x.append(float(line[1]))
            cyc.append(int(line[0]))
    ax1.plot(x,cyc)




plt.show()
