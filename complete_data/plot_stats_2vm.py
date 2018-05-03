import numpy as np
import matplotlib.pyplot as plt


aimd_inrange_1 = [100.0, 100.0, 54.17, 100.0]
aimd_inrange_2 = [100.0, 95.18, 56.34, 100.0]
aimd_cpu_1 = [42.62, 40.41, 40.0, 41.58]
aimd_cpu_2 = [42.5, 46.3, 60.0, 59.33]



apid_inrange_1 = [96.43, 81.13, 77.63, 89.61]
apid_inrange_2 = [98.21, 95.0, 50.82, 94.44]
apid_cpu_1 = [42.17, 40.26, 36.31, 41.28]
apid_cpu_2 = [43.06, 48.62, 58.95, 59.58]



static_inrange_1 = [100.0, 100.0, 2.9, 0.0]
static_inrange_2 = [100.0, 2.74, 0.0, 100.0]
static_cpu_1 = [50.0, 50.0, 50.0, 50.0]
static_cpu_2 = [50.0, 50.0, 50.0, 50.0]


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

exit(0)

ind = np.arange(4)  # the x locations for the groups
width = 0.1  # the width of the bars
patterns = ('*', '+', 'x', '\\', '*', 'o', 'O', '.')


vm1withvm2=0
if vm1withvm2:
	fig, ax = plt.subplots()
	rects1 = ax.bar(ind - width*3.5, rtds_aimd_inrange_1, width*.8,color='b', label='AIMD_vm1',hatch='//')
	rects2 = ax.bar(ind - width*2.5, rtds_aimd_inrange_2, width*.8,color='g', label='AIMD_vm2',hatch='O')
	rects3 = ax.bar(ind - width*1.5, rtds_aimd_inrange_1, width*.8,color='dodgerblue', label='AIMD_vm1',hatch='x')
	rects4 = ax.bar(ind - width*0.5, rtds_aimd_inrange_2, width*.8, color='limegreen', label='AIMD_vm2',hatch='*')
	rects5 = ax.bar(ind + width*0.5, rtds_apid_p95_inrange_1, width*.8,color='skyblue', label='APID_vm1',hatch='//')
	rects6 = ax.bar(ind + width*1.5, rtds_apid_p95_inrange_2, width*.8,color='palegreen', label='APID_vm2',hatch='O')
	rects7 = ax.bar(ind + width*2.5, rtds_static_inrange_1, width*.8,color='darkgrey', label='STATIC_vm1',hatch='x')
	rects8 = ax.bar(ind + width*3.5, rtds_static_inrange_2, width*.8, color='lightgrey', label='STATIC_vm2',hatch='*')

	# Add some text for labels, title and custom x-axis tick labels, etc.
	ax.set_ylabel('Percantage of FPS greater than 10')
	# ax.set_title('Scores by group and gender')
	ax.set_xticks(ind)
	ax.set_xticklabels(('Region 1\nVM1:Medium\nVM2:Medium', 'Region 2\nVM1:Medium\nVM2:Heavy', 'Region 3\nVM1:Heavy\nVM2:Heavy','Region 4\nVM1:Heavy\nVM2:Medium'),fontsize=9)
	ax.legend()

	fig, ax = plt.subplots()
	rects1 = ax.bar(ind - width*3.5, credit_aimd_inrange_1, width*.8,color='b', label='AIMD_vm1',hatch='//')
	rects2 = ax.bar(ind - width*2.5, credit_aimd_inrange_2, width*.8,color='g', label='AIMD_vm2',hatch='O')
	rects3 = ax.bar(ind - width*1.5, credit_aimd_inrange_1, width*.8,color='dodgerblue', label='AIMD_vm1',hatch='x')
	rects4 = ax.bar(ind - width*0.5, credit_aimd_inrange_2, width*.8, color='limegreen', label='AIMD_vm2',hatch='*')
	rects5 = ax.bar(ind + width*0.5, credit_apid_p95_inrange_1, width*.8,color='skyblue', label='APID_vm1',hatch='//')
	rects6 = ax.bar(ind + width*1.5, credit_apid_p95_inrange_2, width*.8,color='palegreen', label='APID_vm2',hatch='O')
	rects7 = ax.bar(ind + width*2.5, credit_static_inrange_1, width*.8,color='darkgrey', label='STATIC_vm1',hatch='x')
	rects8 = ax.bar(ind + width*3.5, credit_static_inrange_2, width*.8, color='lightgrey', label='STATIC_vm2',hatch='*')

	# Add some text for labels, title and custom x-axis tick labels, etc.
	ax.set_ylabel('Percantage of FPS greater than 10')
	# ax.set_title('Scores by group and gender')
	ax.set_xticks(ind)
	ax.set_xticklabels(('Region 1\nVM1:Medium\nVM2:Medium', 'Region 2\nVM1:Medium\nVM2:Heavy', 'Region 3\nVM1:Heavy\nVM2:Heavy','Region 4\nVM1:Heavy\nVM2:Medium'),fontsize=9)
	ax.legend()


	fig, ax = plt.subplots()
	rects1 = ax.bar(ind - width*3.5, rtds_aimd_cpu_1, width*.8,color='b', label='AIMD_vm1',hatch='//')
	rects2 = ax.bar(ind - width*2.5, rtds_aimd_cpu_2, width*.8,color='g', label='AIMD_vm2',hatch='O')
	rects3 = ax.bar(ind - width*1.5, rtds_aimd_cpu_1, width*.8,color='dodgerblue', label='AIMD_vm1',hatch='x')
	rects4 = ax.bar(ind - width*0.5, rtds_aimd_cpu_2, width*.8, color='limegreen', label='AIMD_vm2',hatch='*')
	rects5 = ax.bar(ind + width*0.5, rtds_apid_p95_cpu_1, width*.8,color='skyblue', label='APID_vm1',hatch='//')
	rects6 = ax.bar(ind + width*1.5, rtds_apid_p95_cpu_2, width*.8,color='palegreen', label='APID_vm2',hatch='O')
	rects7 = ax.bar(ind + width*2.5, rtds_static_cpu_1, width*.8,color='darkgrey', label='STATIC_vm1',hatch='x')
	rects8 = ax.bar(ind + width*3.5, rtds_static_cpu_2, width*.8, color='lightgrey', label='STATIC_vm2',hatch='*')

	# Add some text for labels, title and custom x-axis tick labels, etc.
	ax.set_ylabel('CPU Utilization Rate Savings(%)')
	# ax.set_title('Scores by group and gender')
	ax.set_xticks(ind)
	ax.set_xticklabels(('Region 1\nVM1:Medium\nVM2:Medium', 'Region 2\nVM1:Medium\nVM2:Heavy', 'Region 3\nVM1:Heavy\nVM2:Heavy','Region 4\nVM1:Heavy\nVM2:Medium'),fontsize=9)
	ax.legend()

	fig, ax = plt.subplots()
	rects1 = ax.bar(ind - width*3.5, credit_aimd_cpu_1, width*.8,color='b', label='AIMD_vm1',hatch='//')
	rects2 = ax.bar(ind - width*2.5, credit_aimd_cpu_2, width*.8,color='g', label='AIMD_vm2',hatch='O')
	rects3 = ax.bar(ind - width*1.5, credit_aimd_cpu_1, width*.8,color='dodgerblue', label='AIMD_vm1',hatch='x')
	rects4 = ax.bar(ind - width*0.5, credit_aimd_cpu_2, width*.8, color='limegreen', label='AIMD_vm2',hatch='*')
	rects5 = ax.bar(ind + width*0.5, credit_apid_p95_cpu_1, width*.8,color='skyblue', label='APID_vm1',hatch='//')
	rects6 = ax.bar(ind + width*1.5, credit_apid_p95_cpu_2, width*.8,color='palegreen', label='APID_vm2',hatch='O')
	rects7 = ax.bar(ind + width*2.5, credit_static_cpu_1, width*.8,color='darkgrey', label='STATIC_vm1',hatch='x')
	rects8 = ax.bar(ind + width*3.5, credit_static_cpu_2, width*.8, color='lightgrey', label='STATIC_vm2',hatch='*')

	# Add some text for labels, title and custom x-axis tick labels, etc.
	ax.set_ylabel('CPU Utilization Rate Savings(%)')
	# ax.set_title('Scores by group and gender')
	ax.set_xticks(ind)
	ax.set_xticklabels(('Region 1\nVM1:Medium\nVM2:Medium', 'Region 2\nVM1:Medium\nVM2:Heavy', 'Region 3\nVM1:Heavy\nVM2:Heavy','Region 4\nVM1:Heavy\nVM2:Medium'),fontsize=9)
	ax.legend()
else:
	ind = np.arange(4)  # the x locations for the groups
	width = 0.2  # the width of the bars
	patterns = ('*', '+', 'x', '\\', '*', 'o', 'O', '.')
	fig, ax = plt.subplots()
	rects2 = ax.bar(ind - width*1, aimd_inrange_1, width*.8,color='dodgerblue', label='AIMD_VM1',hatch='O')
	rects3 = ax.bar(ind + width*0, apid_inrange_1, width*.8,color='dodgerblue', label='APID_VM1',hatch='//')
	rects4 = ax.bar(ind + width*1, static_inrange_1, width*.8, color='darkgrey', label='STATIC_VM1',hatch='*')
	line = ax.plot([ind[0] - width*1.5,ind[-1] + width*1.5],[100,100],'k')

	# Add some text for labels, title and custom x-axis tick labels, etc.
	ax.set_ylabel('Percantage of FPS greater than 10')
	# ax.set_title('Scores by group and gender')
	ax.set_xticks(ind)
	ax.set_xticklabels(('Region 1\nVM1:Medium\nVM2:Medium', 'Region 2\nVM1:Medium\nVM2:Heavy', 'Region 3\nVM1:Heavy\nVM2:Heavy','Region 4\nVM1:Heavy\nVM2:Medium'),fontsize=9)
	ax.legend(loc='upper center', bbox_to_anchor=(0.5, 1.15),ncol=4, fancybox=True, shadow=False,fontsize=11)

	fig, ax = plt.subplots()
	rects2 = ax.bar(ind - width*1, aimd_inrange_2, width*.8,color='skyblue', label='AIMD_VM2',hatch='O')
	rects3 = ax.bar(ind + width*0, apid_inrange_2, width*.8,color='skyblue', label='APID_VM2',hatch='//')
	rects4 = ax.bar(ind + width*1, static_inrange_2, width*.8, color='lightgrey', label='STATIC_VM2',hatch='*')
	line = ax.plot([ind[0] - width*1.5,ind[-1] + width*1.5],[100,100],'k')

	# Add some text for labels, title and custom x-axis tick labels, etc.
	ax.set_ylabel('Percantage of FPS greater than 10')
	# ax.set_title('Scores by group and gender')
	ax.set_xticks(ind)
	ax.set_xticklabels(('Region 1\nVM1:Medium\nVM2:Medium', 'Region 2\nVM1:Medium\nVM2:Heavy', 'Region 3\nVM1:Heavy\nVM2:Heavy','Region 4\nVM1:Heavy\nVM2:Medium'),fontsize=9)
	ax.legend(loc='upper center', bbox_to_anchor=(0.5, 1.15),ncol=4, fancybox=True, shadow=False,fontsize=11)









	# fig, ax = plt.subplots()
	# rects1 = ax.bar(ind - width*1.5, credit_aimd_inrange_1, width*.8,color='g', label='AIMD_value_VM1',hatch='//')
	# rects2 = ax.bar(ind - width*0.5, credit_aimd_inrange_1, width*.8,color='limegreen', label='AIMD_VM1',hatch='O')
	# rects3 = ax.bar(ind + width*0.5, credit_apid_p95_inrange_1, width*.8,color='palegreen', label='APID_VM1',hatch='x')
	# rects4 = ax.bar(ind + width*1.5, credit_static_inrange_1, width*.8, color='darkgrey', label='STATIC_VM1',hatch='*')

	# # Add some text for labels, title and custom x-axis tick labels, etc.
	# ax.set_ylabel('Percantage of FPS greater than 10')
	# # ax.set_title('Scores by group and gender')
	# ax.set_xticks(ind)
	# ax.set_xticklabels(('Region 1\nVM1:Medium\nVM2:Medium', 'Region 2\nVM1:Medium\nVM2:Heavy', 'Region 3\nVM1:Heavy\nVM2:Heavy','Region 4\nVM1:Heavy\nVM2:Medium'),fontsize=9)
	# ax.legend()


	# fig, ax = plt.subplots()
	# rects1 = ax.bar(ind - width*1.5, credit_aimd_inrange_2, width*.8,color='g', label='AIMD_value_VM2',hatch='\\\\')
	# rects2 = ax.bar(ind - width*0.5, credit_aimd_inrange_2, width*.8,color='limegreen', label='AIMD_VM2',hatch='o')
	# rects3 = ax.bar(ind + width*0.5, credit_apid_p95_inrange_2, width*.8,color='palegreen', label='APID_VM2',hatch='-')
	# rects4 = ax.bar(ind + width*1.5, credit_static_inrange_2, width*.8, color='darkgrey', label='STATIC_VM2',hatch='.')

	# # Add some text for labels, title and custom x-axis tick labels, etc.
	# ax.set_ylabel('Percantage of FPS greater than 10')
	# # ax.set_title('Scores by group and gender')
	# ax.set_xticks(ind)
	# ax.set_xticklabels(('Region 1\nVM1:Medium\nVM2:Medium', 'Region 2\nVM1:Medium\nVM2:Heavy', 'Region 3\nVM1:Heavy\nVM2:Heavy','Region 4\nVM1:Heavy\nVM2:Medium'),fontsize=9)
	# ax.legend()





	# # fig, ax = plt.subplots()
	# # rects1 = ax.bar(ind - width*1.5, rtds_aimd_cpu_1, width*.8,color='b', label='AIMD',hatch='//')
	# # rects2 = ax.bar(ind - width*0.5, rtds_aimd_cpu_1, width*.8,color='dodgerblue', label='AIMD',hatch='O')
	# # rects3 = ax.bar(ind + width*0.5, rtds_apid_p95_cpu_1, width*.8,color='skyblue', label='APID',hatch='x')
	# # rects4 = ax.bar(ind + width*1.5, rtds_static_cpu_1, width*.8, color='darkgrey', label='STATIC',hatch='*')

	# # # Add some text for labels, title and custom x-axis tick labels, etc.
	# # ax.set_ylabel('CPU Utilization Rate Savings(%)')
	# # # ax.set_title('Scores by group and gender')
	# # ax.set_xticks(ind)
	# # ax.set_xticklabels(('Region 1\nVM1:Medium\nVM2:Medium', 'Region 2\nVM1:Medium\nVM2:Heavy', 'Region 3\nVM1:Heavy\nVM2:Heavy','Region 4\nVM1:Heavy\nVM2:Medium'),fontsize=9)
	# # ax.legend()


	# # fig, ax = plt.subplots()
	# # rects1 = ax.bar(ind - width*1.5, rtds_aimd_cpu_2, width*.8,color='b', label='AIMD',hatch='//')
	# # rects2 = ax.bar(ind - width*0.5, rtds_aimd_cpu_2, width*.8,color='dodgerblue', label='AIMD',hatch='O')
	# # rects3 = ax.bar(ind + width*0.5, rtds_apid_p95_cpu_2, width*.8,color='skyblue', label='APID',hatch='x')
	# # rects4 = ax.bar(ind + width*1.5, rtds_static_cpu_2, width*.8, color='darkgrey', label='STATIC',hatch='*')

	# # # Add some text for labels, title and custom x-axis tick labels, etc.
	# # ax.set_ylabel('CPU Utilization Rate Savings(%)')
	# # # ax.set_title('Scores by group and gender')
	# # ax.set_xticks(ind)
	# # ax.set_xticklabels(('Region 1\nVM1:Medium\nVM2:Medium', 'Region 2\nVM1:Medium\nVM2:Heavy', 'Region 3\nVM1:Heavy\nVM2:Heavy','Region 4\nVM1:Heavy\nVM2:Medium'),fontsize=9)
	# # ax.legend()
	# fig, ax = plt.subplots()
	# rects1 = ax.bar(ind - width*1.5, rtds_aimd_cpu_1, width*.8,color='purple', label='AIMD_value_VM1',hatch='//',bottom=rtds_aimd_cpu_2)
	# rects1 = ax.bar(ind - width*1.5, rtds_aimd_cpu_2, width*.8,color='b', label='AIMD_value_VM2',hatch='\\\\')
	# rects2 = ax.bar(ind - width*0.5, rtds_aimd_cpu_1, width*.8,color='pink', label='AIMD_VM1',hatch='O',bottom=rtds_aimd_cpu_2)

	# rects2 = ax.bar(ind - width*0.5, rtds_aimd_cpu_2, width*.8,color='dodgerblue', label='AIMD_VM2',hatch='o')
	# rects3 = ax.bar(ind + width*0.5, rtds_apid_p95_cpu_1, width*.8,color='hotpink', label='APID_VM1',hatch='x',bottom=rtds_apid_p95_cpu_2)

	# rects3 = ax.bar(ind + width*0.5, rtds_apid_p95_cpu_2, width*.8,color='skyblue', label='APID_VM2',hatch='-')
	# rects4 = ax.bar(ind + width*1.5, rtds_static_cpu_1, width*.8, color='dimgrey', label='STATIC_VM1',hatch='*',bottom=rtds_static_cpu_2)

	# rects4 = ax.bar(ind + width*1.5, rtds_static_cpu_2, width*.8, color='lightgrey', label='STATIC_VM2',hatch='.')
	# line = ax.plot([ind[0] - width*2,ind[-1] + width*2],[100,100],'k')
	# # Add some text for labels, title and custom x-axis tick labels, etc.
	# ax.set_ylabel('Average CPU Utilization Rate(%)')
	# # ax.set_title('Scores by group and gender')
	# ax.set_xticks(ind)
	# ax.set_xticklabels(('Region 1\nVM1:Medium\nVM2:Medium', 'Region 2\nVM1:Medium\nVM2:Heavy', 'Region 3\nVM1:Heavy\nVM2:Heavy','Region 4\nVM1:Heavy\nVM2:Medium'),fontsize=9)
	# ax.legend(loc='upper center', bbox_to_anchor=(0.5, 1.15),ncol=4, fancybox=True, shadow=False,fontsize=9)


	# fig, ax = plt.subplots()
	# rects1 = ax.bar(ind - width*1.5, credit_aimd_cpu_1, width*.8,color='purple', label='AIMD_value_VM1',hatch='//',bottom=credit_aimd_cpu_2)
	# rects1 = ax.bar(ind - width*1.5, credit_aimd_cpu_2, width*.8,color='g', label='AIMD_value_VM2',hatch='\\\\')
	# rects2 = ax.bar(ind - width*0.5, credit_aimd_cpu_1, width*.8,color='pink', label='AIMD_VM1',hatch='O',bottom=credit_aimd_cpu_2)

	# rects2 = ax.bar(ind - width*0.5, credit_aimd_cpu_2, width*.8,color='limegreen', label='AIMD_VM2',hatch='o')
	# rects3 = ax.bar(ind + width*0.5, credit_apid_p95_cpu_1, width*.8,color='hotpink', label='APID_VM1',hatch='x',bottom=credit_apid_p95_cpu_2)

	# rects3 = ax.bar(ind + width*0.5, credit_apid_p95_cpu_2, width*.8,color='palegreen', label='APID_VM2',hatch='-')
	# rects4 = ax.bar(ind + width*1.5, credit_static_cpu_1, width*.8, color='dimgrey', label='STATIC_VM1',hatch='*',bottom=credit_static_cpu_2)

	# rects4 = ax.bar(ind + width*1.5, credit_static_cpu_2, width*.8, color='lightgrey', label='STATIC_VM2',hatch='.')
	# line = ax.plot([ind[0] - width*2,ind[-1] + width*2],[100,100],'k')
	# # Add some text for labels, title and custom x-axis tick labels, etc.
	# ax.set_ylabel('Average CPU Utilization Rate(%)')
	# # ax.set_title('Scores by group and gender')
	# ax.set_xticks(ind)
	# ax.set_xticklabels(('Region 1\nVM1:Medium\nVM2:Medium', 'Region 2\nVM1:Medium\nVM2:Heavy', 'Region 3\nVM1:Heavy\nVM2:Heavy','Region 4\nVM1:Heavy\nVM2:Medium'),fontsize=9)
	# ax.legend(loc='upper center', bbox_to_anchor=(0.5, 1.15),ncol=4, fancybox=True, shadow=False,fontsize=9)


	#MSE


	# ind = np.arange(len(credit_aimd_inrange_1))  # the x locations for the groups
	# width = 0.2  # the width of the bars
	# patterns = ('*', '+', 'x', '\\', '*', 'o', 'O', '.')
	# fig, ax = plt.subplots()
	# rects1 = ax.bar(ind - width*1.5, rtds_aimd_mse_1, width*.8,color='b', label='AIMD_value_VM1',hatch='//')
	# rects2 = ax.bar(ind - width*0.5, rtds_aimd_mse_1, width*.8,color='dodgerblue', label='AIMD_VM1',hatch='O')
	# rects3 = ax.bar(ind + width*0.5, rtds_apid_p95_mse_1, width*.8,color='skyblue', label='APID_VM1',hatch='x')
	# rects4 = ax.bar(ind + width*1.5, rtds_static_mse_1, width*.8, color='darkgrey', label='STATIC_VM1',hatch='*')

	# # Add some text for labels, title and custom x-axis tick labels, etc.
	# ax.set_ylabel("Mean Square Error (FPS^2)")
	# # ax.set_title('Scores by group and gender')
	# ax.set_xticks(ind)
	# ax.set_xticklabels(('Region 1\nVM1:Medium\nVM2:Medium', 'Region 2\nVM1:Medium\nVM2:Heavy', 'Region 3\nVM1:Heavy\nVM2:Heavy','Region 4\nVM1:Heavy\nVM2:Medium'),fontsize=9)
	# ax.legend()


	# fig, ax = plt.subplots()
	# rects1 = ax.bar(ind - width*1.5, rtds_aimd_mse_2, width*.8,color='b', label='AIMD_value_VM2',hatch='\\\\')
	# rects2 = ax.bar(ind - width*0.5, rtds_aimd_mse_2, width*.8,color='dodgerblue', label='AIMD_VM2',hatch='o')
	# rects3 = ax.bar(ind + width*0.5, rtds_apid_p95_mse_2, width*.8,color='skyblue', label='APID_VM2',hatch='-')
	# rects4 = ax.bar(ind + width*1.5, rtds_static_mse_2, width*.8, color='darkgrey', label='STATIC_VM2',hatch='.')

	# # Add some text for labels, title and custom x-axis tick labels, etc.
	# ax.set_ylabel("Mean Square Error (FPS^2)")
	# # ax.set_title('Scores by group and gender')
	# ax.set_xticks(ind)
	# ax.set_xticklabels(('Region 1\nVM1:Medium\nVM2:Medium', 'Region 2\nVM1:Medium\nVM2:Heavy', 'Region 3\nVM1:Heavy\nVM2:Heavy','Region 4\nVM1:Heavy\nVM2:Medium'),fontsize=9)
	# ax.legend()



	# fig, ax = plt.subplots()
	# rects1 = ax.bar(ind - width*1.5, credit_aimd_mse_1, width*.8,color='g', label='AIMD_value_VM1',hatch='//')
	# rects2 = ax.bar(ind - width*0.5, credit_aimd_mse_1, width*.8,color='limegreen', label='AIMD_VM1',hatch='O')
	# rects3 = ax.bar(ind + width*0.5, credit_apid_p95_mse_1, width*.8,color='palegreen', label='APID_VM1',hatch='x')
	# rects4 = ax.bar(ind + width*1.5, credit_static_mse_1, width*.8, color='darkgrey', label='STATIC_VM1',hatch='*')

	# # Add some text for labels, title and custom x-axis tick labels, etc.
	# ax.set_ylabel("Mean Square Error (FPS^2)")
	# # ax.set_title('Scores by group and gender')
	# ax.set_xticks(ind)
	# ax.set_xticklabels(('Region 1\nVM1:Medium\nVM2:Medium', 'Region 2\nVM1:Medium\nVM2:Heavy', 'Region 3\nVM1:Heavy\nVM2:Heavy','Region 4\nVM1:Heavy\nVM2:Medium'),fontsize=9)
	# ax.legend()


	# fig, ax = plt.subplots()
	# rects1 = ax.bar(ind - width*1.5, credit_aimd_mse_2, width*.8,color='g', label='AIMD_value_VM2',hatch='\\\\')
	# rects2 = ax.bar(ind - width*0.5, credit_aimd_mse_2, width*.8,color='limegreen', label='AIMD_VM2',hatch='o')
	# rects3 = ax.bar(ind + width*0.5, credit_apid_p95_mse_2, width*.8,color='palegreen', label='APID_VM2',hatch='-')
	# rects4 = ax.bar(ind + width*1.5, credit_static_mse_2, width*.8, color='darkgrey', label='STATIC_VM2',hatch='.')

	# # Add some text for labels, title and custom x-axis tick labels, etc.
	# ax.set_ylabel("Mean Square Error (FPS^2)")
	# # ax.set_title('Scores by group and gender')
	# ax.set_xticks(ind)
	# ax.set_xticklabels(('Region 1\nVM1:Medium\nVM2:Medium', 'Region 2\nVM1:Medium\nVM2:Heavy', 'Region 3\nVM1:Heavy\nVM2:Heavy','Region 4\nVM1:Heavy\nVM2:Medium'),fontsize=9)
	# ax.legend()




plt.show()


