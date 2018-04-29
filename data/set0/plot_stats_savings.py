import numpy as np
import matplotlib.pyplot as plt

aimd_inrange_1 = [100.0, 42.86, 96.77]
aimd_inrange_2 = [99.39, 34.65, 97.58]
aimd_cpu_1 = [7.48, 37.92, 28.06]
aimd_cpu_2 = [5.01, 43.3, 32.47]


aimd_range_inrange_1 = [100.0, 53.47, 97.48]
aimd_range_inrange_2 = [98.84, 45.54, 97.5]
aimd_range_cpu_1 = [0.0, 35.44, 29.93]
aimd_range_cpu_2 = [1.57, 41.67, 36.51]


apid_inrange_1 = [100.0, 85.06, 98.39]
apid_inrange_2 = [97.52, 81.82, 98.39]
apid_cpu_1 = [6.89, 46.02, 28.28]
apid_cpu_2 = [3.81, 52.87, 33.11]


static_inrange_1 = [100.0, 0.0, 0.0]
static_inrange_2 = [91.86, 0.0, 0.0]
static_cpu_1 = [0.0, 0.0, 0.0]
static_cpu_2 = [0.0, 0.0, 0.0]


ind = np.arange(3)  # the x locations for the groups
width = 0.2  # the width of the bars
patterns = ('x', '+', 'x', '\\', '*', 'o', 'O', '*')






fig, ax = plt.subplots()
rects1 = ax.bar(ind - width*1.5, aimd_inrange_1, width*.8,color='b', label='AIMD',hatch='//')
rects2 = ax.bar(ind - width*0.5, aimd_range_inrange_1, width*.8,color='dodgerblue', label='AIMD_range',hatch='O')
rects3 = ax.bar(ind + width*0.5, apid_inrange_1, width*.8,color='skyblue', label='APID',hatch='x')
rects4 = ax.bar(ind + width*1.5, static_inrange_1, width*.8, color='darkgrey', label='STATIC',hatch='*')
line = ax.plot([ind[0] - width*2,ind[-1] + width*2],[100,100],'k')



ax.set_ylabel('Frame Rates within Range (%)')
# ax.set_title('Scores by group and gender')
ax.set_xticks(ind)
ax.set_xticklabels(('Region 1\n(Medium Workload)', 'Region 2\n(Light Workload)', 'Region 3\n(Heavy Workload)'))
ax.legend(loc='upper center', bbox_to_anchor=(0.5, 1.1),ncol=4, fancybox=True, shadow=False)


fig, ax = plt.subplots()
rects1 = ax.bar(ind - width*1.5, aimd_inrange_2, width*.8,color='g', label='AIMD',hatch='//')
rects2 = ax.bar(ind - width*0.5, aimd_range_inrange_2, width*.8,color='limegreen', label='AIMD_range',hatch='O')
rects3 = ax.bar(ind + width*0.5, apid_inrange_2, width*.8,color='palegreen', label='APID',hatch='x')
rects4 = ax.bar(ind + width*1.5, static_inrange_2, width*.8, color='darkgrey', label='STATIC',hatch='*')
line = ax.plot([ind[0] - width*2,ind[-1] + width*2],[100,100],'k')



ax.set_ylabel('Frame Rates within Range (%)')
# ax.set_title('Scores by group and gender')
ax.set_xticks(ind)
ax.set_xticklabels(('Region 1\n(Medium Workload)', 'Region 2\n(Light Workload)', 'Region 3\n(Heavy Workload)'))
ax.legend(loc='upper center', bbox_to_anchor=(0.5, 1.1),ncol=4, fancybox=True, shadow=False)



fig, ax = plt.subplots()
rects1 = ax.bar(ind - width*1, aimd_cpu_1, width*.8,color='b', label='AIMD',hatch='//')
rects2 = ax.bar(ind - width*0, aimd_range_cpu_1, width*.8,color='dodgerblue', label='AIMD_range',hatch='O')
rects3 = ax.bar(ind + width*1, apid_cpu_1, width*.8,color='skyblue', label='APID',hatch='x')
line = ax.plot([ind[0] - width*1.5,ind[-1] + width*1.5],[100,100],'k')

# rects4 = ax.bar(ind + width*1.5, static_cpu_1, width*.8, color='darkgrey', label='STATIC',hatch='*')



ax.set_ylabel('Average CPU Utilization Rate Savings(%)')
# ax.set_title('Scores by group and gender')
ax.set_xticks(ind)
ax.set_xticklabels(('Region 1\n(Medium Workload)', 'Region 2\n(Light Workload)', 'Region 3\n(Heavy Workload)'))
ax.legend(loc='upper center', bbox_to_anchor=(0.5, 1.1),ncol=3, fancybox=True, shadow=False)


fig, ax = plt.subplots()
rects1 = ax.bar(ind - width*1, aimd_cpu_2, width*.8,color='g', label='AIMD',hatch='//')
rects2 = ax.bar(ind - width*0, aimd_range_cpu_2, width*.8,color='limegreen', label='AIMD_range',hatch='O')
rects3 = ax.bar(ind + width*1, apid_cpu_2, width*.8,color='palegreen', label='APID',hatch='x')
line = ax.plot([ind[0] - width*1.5,ind[-1] + width*1.5],[100,100],'k')

# rects4 = ax4.bar(ind + width*1.5, static_cpu_2, width*.8, color='darkgrey', label='STATIC',hatch='*')



ax.set_ylabel('Average CPU Utilization Rate Savings(%)')
# ax.set_title('Scores by group and gender')
ax.set_xticks(ind)
ax.set_xticklabels(('Region 1\n(Medium Workload)', 'Region 2\n(Light Workload)', 'Region 3\n(Heavy Workload)'))
ax.legend(loc='upper center', bbox_to_anchor=(0.5, 1.1),ncol=3, fancybox=True, shadow=False)

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


