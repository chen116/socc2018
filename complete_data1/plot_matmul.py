from os import listdir
from os.path import isfile, join
import sys
rand=sys.argv[1]

onlyfiles = [f for f in listdir('./') if isfile(join('./', f))]
# print(onlyfiles)
files = [ f for f in onlyfiles if "mul_" in f]
# if "r" in rand:
#     files = [ f for f in onlyfiles if "mul_" in f]




import matplotlib.pyplot as plt
import matplotlib.animation as animation
from matplotlib.widgets import Cursor
from matplotlib.font_manager import FontProperties
from matplotlib.widgets import CheckButtons
import numpy as np
import time
# fig = plt.figure(figsize=(10, 7))
# ax1 = fig.add_subplot(1,1,1)



fcnt=0
color=['r--','g:','k-']
ncc=[]
for f in files:
    x = []
    cyc = []
    pullData = open(f,"r").read()
    dataArray = pullData.split('\n')
    for eachLine in dataArray:
        if len(eachLine)>1:
            line = eachLine.split()
            x.append(float(line[1]))
            cyc.append(int(line[0]))
    ncc.append(cyc[-1])
    # ax1.plot(x,cyc,color[fcnt],label= f)
    # ax1.legend()
    # ax1.set_xlabel('Time(seconds)')
    # ax1.set_ylabel('Number of Computations Completed')
    fcnt+=1


ind = np.arange(1)  # the x locations for the groups
width = 0.2  # the width of the bars
patterns = ('*', '+', 'x', '\\', '*', 'o', 'O', '.')




fig, ax = plt.subplots()
rects2 = ax.bar(ind - width*1, ncc[0], width*.8,color='red', label='AIMD',hatch='O')
rects3 = ax.bar(ind + width*0, ncc[1], width*.8,color='m', label='APID',hatch='//')
rects4 = ax.bar(ind + width*1, ncc[2], width*.8, color='darkgrey', label='STATIC',hatch='*')
for i, v in enumerate(ncc):
    ax.text(ind  + width*(i-1.1),v, str(v), color='k', fontweight='bold')
# line = ax.plot([ind[0] - width*1.5,ind[-1] + width*1.5],[100,100],'k')

# Add some text for labels, title and custom x-axis tick labels, etc.
ax.set_ylabel('Number of Computations Completed')
# ax.set_title('Scores by group and gender')
ax.set_xticks([])
# ax.set_xticklabels(['Number of Computations Completed'],fontsize=9)
ax.legend(loc='upper center', bbox_to_anchor=(0.5, 1.15),ncol=4, fancybox=True, shadow=False,fontsize=11)


plt.show()
