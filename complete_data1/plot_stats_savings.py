import numpy as np
import matplotlib.pyplot as plt



aimd_inrange_1 = [100.0, 100.0, 96.3]
aimd_inrange_2 = [100.0, 100.0, 96.3]
aimd_cpu_1 = [5.84, 48.77, 36.83]
aimd_cpu_2 = [2.49, 52.56, 42.35]




aimd_inrange_1 = [100.0, 100.0, 96.36]
aimd_inrange_2 = [97.81, 97.47, 96.33]
aimd_cpu_1 = [6.88, 51.92, 37.0]
aimd_cpu_2 = [5.58, 57.19, 42.74]


apid_11p0_inrange_1 = [100.0, 97.37, 96.49]
apid_11p0_inrange_2 = [99.3, 93.59, 97.32]
apid_11p0_cpu_1 = [11.3, 54.9, 35.5]
apid_11p0_cpu_2 = [3.33, 57.16, 36.75]


static_inrange_1 = [100.0, 100.0, 100.0]
static_inrange_2 = [100.0, 100.0, 100.0]
static_cpu_1 = [0.0, 0.0, 0.0]
static_cpu_2 = [0.0, 0.0, 0.0]



s='AIMD'
for i in aimd_cpu_1:
	s+=('& '+str(i)+'\\% ')
print(s+ ' \\\\ \\hline')
s='APID'
for i in apid_cpu_1:
	s+=('& '+str(i)+'\\% ')
print(s+ ' \\\\ \\hline')

print('')
s='AIMD'
for i in aimd_cpu_2:
	s+=('& '+str(i)+'\\% ')
print(s+ ' \\\\ \\hline')
s='APID'
for i in apid_cpu_2:
	s+=('& '+str(i)+'\\% ')
print(s+ ' \\\\ \\hline')

print('')
s='STATIC'
for i in static_inrange_1:
	s+=('& '+str(i)+'\\% ')
print(s+ ' \\\\ \\hline')
s='AIMD'
for i in aimd_inrange_1:
	s+=('& '+str(i)+'\\% ')
print(s+ ' \\\\ \\hline')
s='APID'
for i in apid_inrange_1:
	s+=('& '+str(i)+'\\% ')
print(s+ ' \\\\ \\hline')

print('')
s='STATIC'
for i in static_inrange_2:
	s+=('& '+str(i)+'\\% ')
print(s+ ' \\\\ \\hline')
s='AIMD'
for i in aimd_inrange_2:
	s+=('& '+str(i)+'\\% ')
print(s+ ' \\\\ \\hline')
s='APID'
for i in apid_inrange_2:
	s+=('& '+str(i)+'\\% ')
print(s+ ' \\\\ \\hline')





ind = np.arange(3)  # the x locations for the groups
width = 0.2  # the width of the bars
patterns = ("//", '+', "o", '\\', '*', 'o', 'O', '*')






fig, ax = plt.subplots()
rects1 = ax.bar(ind - width*1, aimd_inrange_1, width*.8,color='b', label='AIMD',hatch='O')
# rects2 = ax.bar(ind - width*0.5, aimd_range_inrange_1, width*.8,color='dodgerblue', label='AIMD_range',hatch='O')
rects3 = ax.bar(ind + width*0., apid_inrange_1, width*.8,color='skyblue', label='APID',hatch="//")
rects4 = ax.bar(ind + width*1, static_inrange_1, width*.8, color='darkgrey', label='STATIC',hatch='*')
line = ax.plot([ind[0] - width*2,ind[-1] + width*2],[100,100],'k')



ax.set_ylabel('Percantage of FPS greater than 10')

# ax.set_title('Scores by group and gender')
ax.set_xticks(ind)
ax.set_xticklabels(('Region 1\n(Heavy Workload)', 'Region 2\n(Light Workload)', 'Region 3\n(Medium Workload)'))
ax.legend(loc='upper center', bbox_to_anchor=(0.5, 1.1),ncol=4, fancybox=True, shadow=False,fontsize=10)


fig, ax = plt.subplots()
rects1 = ax.bar(ind - width*1, aimd_inrange_2, width*.8,color='g', label='AIMD',hatch='O')
# rects2 = ax.bar(ind - width*0.5, aimd_range_inrange_2, width*.8,color='limegreen', label='AIMD_range',hatch='O')
rects3 = ax.bar(ind + width*0., apid_inrange_2, width*.8,color='palegreen', label='APID',hatch="//")
rects4 = ax.bar(ind + width*1, static_inrange_2, width*.8, color='darkgrey', label='STATIC',hatch='*')
line = ax.plot([ind[0] - width*2,ind[-1] + width*2],[100,100],'k')



ax.set_ylabel('Percantage of FPS greater than 10')
# ax.set_title('Scores by group and gender')
ax.set_xticks(ind)
ax.set_xticklabels(('Region 1\n(Heavy Workload)', 'Region 2\n(Light Workload)', 'Region 3\n(Medium Workload)'))
ax.legend(loc='upper center', bbox_to_anchor=(0.5, 1.1),ncol=4, fancybox=True, shadow=False,fontsize=10)



fig, ax = plt.subplots()
rects1 = ax.bar(ind - width*.5, aimd_cpu_1, width*.8,color='b', label='AIMD',hatch='O')
# rects2 = ax.bar(ind - width*0, aimd_range_cpu_1, width*.8,color='dodgerblue', label='AIMD_range',hatch='O')
rects3 = ax.bar(ind + width*.5, apid_cpu_1, width*.8,color='skyblue', label='APID',hatch="//")
# line = ax.plot([ind[0] - width*1.5,ind[-1] + width*1.5],[100,100],'k')

# rects4 = ax.bar(ind + width*1.5, static_cpu_1, width*.8, color='darkgrey', label='STATIC',hatch='*')



ax.set_ylabel('Average CPU Utilization Rate Savings(%)')
ax.set_ylim([0,60])

# ax.set_title('Scores by group and gender')
ax.set_xticks(ind)
ax.set_xticklabels(('Region 1\n(Heavy Workload)', 'Region 2\n(Light Workload)', 'Region 3\n(Medium Workload)'))
ax.legend()

fig, ax = plt.subplots()
rects1 = ax.bar(ind - width*.5, aimd_cpu_2, width*.8,color='g', label='AIMD',hatch='O')
# rects2 = ax.bar(ind - width*0, aimd_range_cpu_2, width*.8,color='limegreen', label='AIMD_range',hatch='O')
rects3 = ax.bar(ind + width*.5, apid_cpu_2, width*.8,color='palegreen', label='APID',hatch="//")
# line = ax.plot([ind[0] - width*1.5,ind[-1] + width*1.5],[100,100],'k')

# rects4 = ax4.bar(ind + width*1.5, static_cpu_2, width*.8, color='darkgrey', label='STATIC',hatch='*')



ax.set_ylabel('Average CPU Utilization Rate Savings(%)')
ax.set_ylim([0,60])

# ax.set_title('Scores by group and gender')
ax.set_xticks(ind)
ax.set_xticklabels(('Region 1\n(Heavy Workload)', 'Region 2\n(Light Workload)', 'Region 3\n(Medium Workload)'))
# ax.legend(loc='upper center', bbox_to_anchor=(0.5, 1.1),ncol=3, fancybox=True, shadow=False,fontsize=10)
ax.legend()
# def autolabel(rects, xpos='center'):
#     """
#     Attach a text label above each bar in *rects*, displaying its height.

#     *xpos* indicates which side to place the text w.r.t. the center of
#     the bar. It can be one of the following {'center', 'right', 'left'}.
#     """

#     xpos = xpos.lower()  # normalize the case of the parameter
#     ha = {'center': 'center', 'right': 'left', 'left': 'right'}
#     offset = {'center': 0.5, 'right': 0.57, 'left': 0.43}  # x_txt = x + w*off

#     for rect in rects:
#         height = rect.get_height()
#         ax.text(rect.get_x() + rect.get_width()*offset[xpos], 1.01*height,
#                 '{}'.format(height), ha=ha[xpos], va='bottom')
# autolabel(rects1, "left")
# autolabel(rects2, "right")

plt.show()


