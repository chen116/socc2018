import numpy as np
import matplotlib.pyplot as plt
import sys

aimd_tb_hr_above_min= [98.39, 98.41]
aimd_tb_cpu_use= [36.61, 35.86]


apid_tb_hr_above_min= [97.83, 96.79]
apid_tb_cpu_use= [36.24, 35.58]


static_tb_hr_above_min= [100.0, 100.0]
static_tb_cpu_use= [45.0, 45.0]



aimd_tb_hr_above_min= [91.86, 96.34]
aimd_tb_cpu_use= [33.67, 31.52]


apid_tb_rand_hr_above_min= [91.48, 93.02]
apid_tb_rand_cpu_use= [34.97, 33.17]


static_tb_rand_hr_above_min= [100.0, 100.0]
static_tb_rand_cpu_use= [45.0, 45.0]


# rand
rand=sys.argv[1]
if "r" in rand:
	aimd_tb_hr_above_min= [94.89, 96.47]
	aimd_tb_cpu_use= [34.99, 32.73]


	apid_tb_hr_above_min= [91.48, 93.02]
	apid_tb_cpu_use= [34.97, 33.17]


	static_tb_hr_above_min= [100.0, 100.0]
	static_tb_cpu_use= [45.0, 45.0]

s='STATIC'
for i in static_tb_hr_above_min:
	s+=('& '+str(i)+'\\% ')
print(s+ ' \\\\ \\hline')
s='AIMD'
for i in aimd_tb_hr_above_min:
	s+=('& '+str(i)+'\\% ')
print(s+ ' \\\\ \\hline')
s='APID'
for i in apid_tb_hr_above_min:
	s+=('& '+str(i)+'\\% ')
print(s+ ' \\\\ \\hline')

exit(0)

ind = np.arange(2)  # the x locations for the groups
width = 0.2  # the width of the bars
patterns = ('*', '+', 'x', '\\', '*', 'o', 'O', '.')




fig, ax = plt.subplots()
rects2 = ax.bar(ind - width*1, aimd_tb_hr_above_min, width*.8,color='dodgerblue', label='AIMD',hatch='O')
rects3 = ax.bar(ind + width*0, apid_tb_hr_above_min, width*.8,color='skyblue', label='APID',hatch='//')
rects4 = ax.bar(ind + width*1, static_tb_hr_above_min, width*.8, color='darkgrey', label='STATIC',hatch='*')
line = ax.plot([ind[0] - width*1.5,ind[-1] + width*1.5],[100,100],'k')

# for i, v in enumerate(ncc):
#     ax.text(ind  + width*(i-1.1),v, str(v), color='k', fontweight='bold')
# line = ax.plot([ind[0] - width*1.5,ind[-1] + width*1.5],[100,100],'k')

# Add some text for labels, title and custom x-axis tick labels, etc.
ax.set_ylabel('Percantage of FPS greater than 10')
# ax.set_title('Scores by group and gender')
ax.set_xticks(ind)
ax.set_xticklabels(('VM1','VM2'),fontsize=9)
ax.legend(loc='upper center', bbox_to_anchor=(0.5, 1.15),ncol=4, fancybox=True, shadow=False,fontsize=11)


plt.show()

