import numpy as np
import matplotlib.pyplot as plt

credit_aimd_inrange_1 = [94.29, 48.72, 35.56, 50.0]
credit_aimd_inrange_2 = [98.63, 47.0, 48.0, 47.95]



credit_aimd_range_inrange_1 = [100.0, 48.1, 51.72, 60.4]
credit_aimd_range_inrange_2 = [100.0, 60.91, 58.89, 36.99]



credit_apid_p95_inrange_1 = [100.0, 58.9, 0.0, 3.49]
credit_apid_p95_inrange_2 = [100.0, 23.75, 0.0, 63.77]


credit_static_inrange_1 = [100.0, 100.0, 0.0, 0.0]
credit_static_inrange_2 = [100.0, 0.0, 0.0, 98.59]


rtds_aimd_inrange_1 = [79.17, 42.11, 31.52, 53.77]
rtds_aimd_inrange_2 = [80.82, 58.49, 28.72, 43.84]



rtds_aimd_range_inrange_1 = [100.0, 45.21, 52.53, 52.63]
rtds_aimd_range_inrange_2 = [100.0, 63.81, 47.37, 54.79]



rtds_apid_p95_inrange_1 = [100.0, 67.09, 0.0, 0.0]
rtds_apid_p95_inrange_2 = [100.0, 0.0, 0.0, 39.73]



rtds_static_inrange_1 = [100.0, 100.0, 0.0, 0.0]
rtds_static_inrange_2 = [100.0, 0.0, 0.0, 98.63]


credit_aimd_cpu_1 = [48.15, 41.72, 47.74, 57.63]
credit_aimd_cpu_2 = [49.78, 57.84, 51.95, 41.94]


credit_aimd_range_cpu_1 = [50.0, 40.11, 49.94, 58.28]
credit_aimd_range_cpu_2 = [50.0, 59.88, 50.06, 41.65]


credit_apid_p95_cpu_1 = [49.68, 45.63, 48.6, 56.34]
credit_apid_p95_cpu_2 = [49.65, 52.75, 51.4, 43.66]


credit_static_cpu_1 = [50.0, 50.0, 50.0, 50.0]
credit_static_cpu_2 = [50.0, 50.0, 50.0, 50.0]


rtds_aimd_cpu_1 = [49.19, 40.2, 49.91, 58.97]
rtds_aimd_cpu_2 = [50.27, 59.37, 50.03, 40.54]


rtds_aimd_range_cpu_1 = [50.0, 38.48, 51.92, 56.14]
rtds_aimd_range_cpu_2 = [50.0, 61.52, 48.08, 43.85]


rtds_apid_p95_cpu_1 = [50.01, 46.46, 50.45, 55.06]
rtds_apid_p95_cpu_2 = [49.98, 53.54, 49.55, 44.94]


rtds_static_cpu_1 = [50.0, 50.0, 50.0, 50.0]
rtds_static_cpu_2 = [50.0, 50.0, 50.0, 50.0]



credit_aimd_mse_1 = [0.0, 1.53, 4.37, 0.83]
credit_aimd_mse_2 = [0.0, 0.92, 2.51, 1.86]


credit_aimd_range_mse_1 = [0.0, 2.06, 4.2, 0.74]
credit_aimd_range_mse_2 = [0.0, 0.69, 3.77, 1.61]


credit_apid_p95_mse_1 = [0.0, 2.8, 2.14, 0.27]
credit_apid_p95_mse_2 = [0.0, 2.54, 0.99, 0.03]


credit_static_mse_1 = [0.0, 0.0, 1.33, 1.15]
credit_static_mse_2 = [0.0, 1.2, 1.34, 0.02]


rtds_aimd_mse_1 = [0.01, 2.51, 2.97, 1.1]
rtds_aimd_mse_2 = [0.02, 0.73, 3.07, 2.91]


rtds_aimd_range_mse_1 = [0.0, 2.74, 4.27, 1.17]
rtds_aimd_range_mse_2 = [0.0, 0.73, 4.7, 1.73]


rtds_apid_p95_mse_1 = [0.0, 0.01, 1.92, 0.59]
rtds_apid_p95_mse_2 = [0.0, 0.72, 1.57, 0.08]


rtds_static_mse_1 = [0.0, 0.0, 1.63, 1.56]
rtds_static_mse_2 = [0.0, 1.61, 1.51, 0.02]

ind = np.arange(4)  # the x locations for the groups
width = 0.1  # the width of the bars
patterns = ('*', '+', 'x', '\\', '*', 'o', 'O', '.')


vm1withvm2=0
if vm1withvm2:
	fig, ax = plt.subplots()
	rects1 = ax.bar(ind - width*3.5, rtds_aimd_inrange_1, width*.8,color='b', label='AIMD_vm1',hatch='//')
	rects2 = ax.bar(ind - width*2.5, rtds_aimd_inrange_2, width*.8,color='g', label='AIMD_vm2',hatch='O')
	rects3 = ax.bar(ind - width*1.5, rtds_aimd_range_inrange_1, width*.8,color='dodgerblue', label='AIMD_range_vm1',hatch='x')
	rects4 = ax.bar(ind - width*0.5, rtds_aimd_range_inrange_2, width*.8, color='limegreen', label='AIMD_range_vm2',hatch='*')
	rects5 = ax.bar(ind + width*0.5, rtds_apid_p95_inrange_1, width*.8,color='skyblue', label='APID_vm1',hatch='//')
	rects6 = ax.bar(ind + width*1.5, rtds_apid_p95_inrange_2, width*.8,color='palegreen', label='APID_vm2',hatch='O')
	rects7 = ax.bar(ind + width*2.5, rtds_static_inrange_1, width*.8,color='darkgrey', label='STATIC_vm1',hatch='x')
	rects8 = ax.bar(ind + width*3.5, rtds_static_inrange_2, width*.8, color='lightgrey', label='STATIC_vm2',hatch='*')

	# Add some text for labels, title and custom x-axis tick labels, etc.
	ax.set_ylabel('Frame Rates within Range (%)')
	# ax.set_title('Scores by group and gender')
	ax.set_xticks(ind)
	ax.set_xticklabels(('Region 1\nVM1:Medium\nVM2:Medium', 'Region 2\nVM1:Medium\nVM2:Heavy', 'Region 3\nVM1:Heavy\nVM2:Heavy','Region 4\nVM1:Heavy\nVM2:Medium'),fontsize=9)
	ax.legend()

	fig, ax = plt.subplots()
	rects1 = ax.bar(ind - width*3.5, credit_aimd_inrange_1, width*.8,color='b', label='AIMD_vm1',hatch='//')
	rects2 = ax.bar(ind - width*2.5, credit_aimd_inrange_2, width*.8,color='g', label='AIMD_vm2',hatch='O')
	rects3 = ax.bar(ind - width*1.5, credit_aimd_range_inrange_1, width*.8,color='dodgerblue', label='AIMD_range_vm1',hatch='x')
	rects4 = ax.bar(ind - width*0.5, credit_aimd_range_inrange_2, width*.8, color='limegreen', label='AIMD_range_vm2',hatch='*')
	rects5 = ax.bar(ind + width*0.5, credit_apid_p95_inrange_1, width*.8,color='skyblue', label='APID_vm1',hatch='//')
	rects6 = ax.bar(ind + width*1.5, credit_apid_p95_inrange_2, width*.8,color='palegreen', label='APID_vm2',hatch='O')
	rects7 = ax.bar(ind + width*2.5, credit_static_inrange_1, width*.8,color='darkgrey', label='STATIC_vm1',hatch='x')
	rects8 = ax.bar(ind + width*3.5, credit_static_inrange_2, width*.8, color='lightgrey', label='STATIC_vm2',hatch='*')

	# Add some text for labels, title and custom x-axis tick labels, etc.
	ax.set_ylabel('Frame Rates within Range (%)')
	# ax.set_title('Scores by group and gender')
	ax.set_xticks(ind)
	ax.set_xticklabels(('Region 1\nVM1:Medium\nVM2:Medium', 'Region 2\nVM1:Medium\nVM2:Heavy', 'Region 3\nVM1:Heavy\nVM2:Heavy','Region 4\nVM1:Heavy\nVM2:Medium'),fontsize=9)
	ax.legend()


	fig, ax = plt.subplots()
	rects1 = ax.bar(ind - width*3.5, rtds_aimd_cpu_1, width*.8,color='b', label='AIMD_vm1',hatch='//')
	rects2 = ax.bar(ind - width*2.5, rtds_aimd_cpu_2, width*.8,color='g', label='AIMD_vm2',hatch='O')
	rects3 = ax.bar(ind - width*1.5, rtds_aimd_range_cpu_1, width*.8,color='dodgerblue', label='AIMD_range_vm1',hatch='x')
	rects4 = ax.bar(ind - width*0.5, rtds_aimd_range_cpu_2, width*.8, color='limegreen', label='AIMD_range_vm2',hatch='*')
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
	rects3 = ax.bar(ind - width*1.5, credit_aimd_range_cpu_1, width*.8,color='dodgerblue', label='AIMD_range_vm1',hatch='x')
	rects4 = ax.bar(ind - width*0.5, credit_aimd_range_cpu_2, width*.8, color='limegreen', label='AIMD_range_vm2',hatch='*')
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
	ind = np.arange(len(credit_aimd_inrange_1))  # the x locations for the groups
	width = 0.2  # the width of the bars
	patterns = ('*', '+', 'x', '\\', '*', 'o', 'O', '.')
	fig, ax = plt.subplots()
	rects1 = ax.bar(ind - width*1.5, rtds_aimd_inrange_1, width*.8,color='b', label='AIMD_value_VM1',hatch='//')
	rects2 = ax.bar(ind - width*0.5, rtds_aimd_range_inrange_1, width*.8,color='dodgerblue', label='AIMD_range_VM1',hatch='O')
	rects3 = ax.bar(ind + width*0.5, rtds_apid_p95_inrange_1, width*.8,color='skyblue', label='APID_VM1',hatch='x')
	rects4 = ax.bar(ind + width*1.5, rtds_static_inrange_1, width*.8, color='darkgrey', label='STATIC_VM1',hatch='*')

	# Add some text for labels, title and custom x-axis tick labels, etc.
	ax.set_ylabel('Frame Rates within Range (%)')
	# ax.set_title('Scores by group and gender')
	ax.set_xticks(ind)
	ax.set_xticklabels(('Region 1\nVM1:Medium\nVM2:Medium', 'Region 2\nVM1:Medium\nVM2:Heavy', 'Region 3\nVM1:Heavy\nVM2:Heavy','Region 4\nVM1:Heavy\nVM2:Medium'),fontsize=9)
	ax.legend()


	fig, ax = plt.subplots()
	rects1 = ax.bar(ind - width*1.5, rtds_aimd_inrange_2, width*.8,color='b', label='AIMD_value_VM2',hatch='\\\\')
	rects2 = ax.bar(ind - width*0.5, rtds_aimd_range_inrange_2, width*.8,color='dodgerblue', label='AIMD_range_VM2',hatch='o')
	rects3 = ax.bar(ind + width*0.5, rtds_apid_p95_inrange_2, width*.8,color='skyblue', label='APID_VM2',hatch='-')
	rects4 = ax.bar(ind + width*1.5, rtds_static_inrange_2, width*.8, color='darkgrey', label='STATIC_VM2',hatch='.')

	# Add some text for labels, title and custom x-axis tick labels, etc.
	ax.set_ylabel('Frame Rates within Range (%)')
	# ax.set_title('Scores by group and gender')
	ax.set_xticks(ind)
	ax.set_xticklabels(('Region 1\nVM1:Medium\nVM2:Medium', 'Region 2\nVM1:Medium\nVM2:Heavy', 'Region 3\nVM1:Heavy\nVM2:Heavy','Region 4\nVM1:Heavy\nVM2:Medium'),fontsize=9)
	ax.legend()



	fig, ax = plt.subplots()
	rects1 = ax.bar(ind - width*1.5, credit_aimd_inrange_1, width*.8,color='g', label='AIMD_value_VM1',hatch='//')
	rects2 = ax.bar(ind - width*0.5, credit_aimd_range_inrange_1, width*.8,color='limegreen', label='AIMD_range_VM1',hatch='O')
	rects3 = ax.bar(ind + width*0.5, credit_apid_p95_inrange_1, width*.8,color='palegreen', label='APID_VM1',hatch='x')
	rects4 = ax.bar(ind + width*1.5, credit_static_inrange_1, width*.8, color='darkgrey', label='STATIC_VM1',hatch='*')

	# Add some text for labels, title and custom x-axis tick labels, etc.
	ax.set_ylabel('Frame Rates within Range (%)')
	# ax.set_title('Scores by group and gender')
	ax.set_xticks(ind)
	ax.set_xticklabels(('Region 1\nVM1:Medium\nVM2:Medium', 'Region 2\nVM1:Medium\nVM2:Heavy', 'Region 3\nVM1:Heavy\nVM2:Heavy','Region 4\nVM1:Heavy\nVM2:Medium'),fontsize=9)
	ax.legend()


	fig, ax = plt.subplots()
	rects1 = ax.bar(ind - width*1.5, credit_aimd_inrange_2, width*.8,color='g', label='AIMD_value_VM2',hatch='\\\\')
	rects2 = ax.bar(ind - width*0.5, credit_aimd_range_inrange_2, width*.8,color='limegreen', label='AIMD_range_VM2',hatch='o')
	rects3 = ax.bar(ind + width*0.5, credit_apid_p95_inrange_2, width*.8,color='palegreen', label='APID_VM2',hatch='-')
	rects4 = ax.bar(ind + width*1.5, credit_static_inrange_2, width*.8, color='darkgrey', label='STATIC_VM2',hatch='.')

	# Add some text for labels, title and custom x-axis tick labels, etc.
	ax.set_ylabel('Frame Rates within Range (%)')
	# ax.set_title('Scores by group and gender')
	ax.set_xticks(ind)
	ax.set_xticklabels(('Region 1\nVM1:Medium\nVM2:Medium', 'Region 2\nVM1:Medium\nVM2:Heavy', 'Region 3\nVM1:Heavy\nVM2:Heavy','Region 4\nVM1:Heavy\nVM2:Medium'),fontsize=9)
	ax.legend()





	# fig, ax = plt.subplots()
	# rects1 = ax.bar(ind - width*1.5, rtds_aimd_cpu_1, width*.8,color='b', label='AIMD',hatch='//')
	# rects2 = ax.bar(ind - width*0.5, rtds_aimd_range_cpu_1, width*.8,color='dodgerblue', label='AIMD_range',hatch='O')
	# rects3 = ax.bar(ind + width*0.5, rtds_apid_p95_cpu_1, width*.8,color='skyblue', label='APID',hatch='x')
	# rects4 = ax.bar(ind + width*1.5, rtds_static_cpu_1, width*.8, color='darkgrey', label='STATIC',hatch='*')

	# # Add some text for labels, title and custom x-axis tick labels, etc.
	# ax.set_ylabel('CPU Utilization Rate Savings(%)')
	# # ax.set_title('Scores by group and gender')
	# ax.set_xticks(ind)
	# ax.set_xticklabels(('Region 1\nVM1:Medium\nVM2:Medium', 'Region 2\nVM1:Medium\nVM2:Heavy', 'Region 3\nVM1:Heavy\nVM2:Heavy','Region 4\nVM1:Heavy\nVM2:Medium'),fontsize=9)
	# ax.legend()


	# fig, ax = plt.subplots()
	# rects1 = ax.bar(ind - width*1.5, rtds_aimd_cpu_2, width*.8,color='b', label='AIMD',hatch='//')
	# rects2 = ax.bar(ind - width*0.5, rtds_aimd_range_cpu_2, width*.8,color='dodgerblue', label='AIMD_range',hatch='O')
	# rects3 = ax.bar(ind + width*0.5, rtds_apid_p95_cpu_2, width*.8,color='skyblue', label='APID',hatch='x')
	# rects4 = ax.bar(ind + width*1.5, rtds_static_cpu_2, width*.8, color='darkgrey', label='STATIC',hatch='*')

	# # Add some text for labels, title and custom x-axis tick labels, etc.
	# ax.set_ylabel('CPU Utilization Rate Savings(%)')
	# # ax.set_title('Scores by group and gender')
	# ax.set_xticks(ind)
	# ax.set_xticklabels(('Region 1\nVM1:Medium\nVM2:Medium', 'Region 2\nVM1:Medium\nVM2:Heavy', 'Region 3\nVM1:Heavy\nVM2:Heavy','Region 4\nVM1:Heavy\nVM2:Medium'),fontsize=9)
	# ax.legend()
	fig, ax = plt.subplots()
	rects1 = ax.bar(ind - width*1.5, rtds_aimd_cpu_1, width*.8,color='purple', label='AIMD_value_VM1',hatch='//',bottom=rtds_aimd_cpu_2)
	rects1 = ax.bar(ind - width*1.5, rtds_aimd_cpu_2, width*.8,color='b', label='AIMD_value_VM2',hatch='\\\\')
	rects2 = ax.bar(ind - width*0.5, rtds_aimd_range_cpu_1, width*.8,color='pink', label='AIMD_range_VM1',hatch='O',bottom=rtds_aimd_range_cpu_2)

	rects2 = ax.bar(ind - width*0.5, rtds_aimd_range_cpu_2, width*.8,color='dodgerblue', label='AIMD_range_VM2',hatch='o')
	rects3 = ax.bar(ind + width*0.5, rtds_apid_p95_cpu_1, width*.8,color='hotpink', label='APID_VM1',hatch='x',bottom=rtds_apid_p95_cpu_2)

	rects3 = ax.bar(ind + width*0.5, rtds_apid_p95_cpu_2, width*.8,color='skyblue', label='APID_VM2',hatch='-')
	rects4 = ax.bar(ind + width*1.5, rtds_static_cpu_1, width*.8, color='dimgrey', label='STATIC_VM1',hatch='*',bottom=rtds_static_cpu_2)

	rects4 = ax.bar(ind + width*1.5, rtds_static_cpu_2, width*.8, color='lightgrey', label='STATIC_VM2',hatch='.')
	line = ax.plot([ind[0] - width*2,ind[-1] + width*2],[100,100],'k')
	# Add some text for labels, title and custom x-axis tick labels, etc.
	ax.set_ylabel('Average CPU Utilization Rate(%)')
	# ax.set_title('Scores by group and gender')
	ax.set_xticks(ind)
	ax.set_xticklabels(('Region 1\nVM1:Medium\nVM2:Medium', 'Region 2\nVM1:Medium\nVM2:Heavy', 'Region 3\nVM1:Heavy\nVM2:Heavy','Region 4\nVM1:Heavy\nVM2:Medium'),fontsize=9)
	ax.legend(loc='upper center', bbox_to_anchor=(0.5, 1.15),ncol=4, fancybox=True, shadow=False,fontsize=9)


	fig, ax = plt.subplots()
	rects1 = ax.bar(ind - width*1.5, credit_aimd_cpu_1, width*.8,color='purple', label='AIMD_value_VM1',hatch='//',bottom=credit_aimd_cpu_2)
	rects1 = ax.bar(ind - width*1.5, credit_aimd_cpu_2, width*.8,color='g', label='AIMD_value_VM2',hatch='\\\\')
	rects2 = ax.bar(ind - width*0.5, credit_aimd_range_cpu_1, width*.8,color='pink', label='AIMD_range_VM1',hatch='O',bottom=credit_aimd_range_cpu_2)

	rects2 = ax.bar(ind - width*0.5, credit_aimd_range_cpu_2, width*.8,color='limegreen', label='AIMD_range_VM2',hatch='o')
	rects3 = ax.bar(ind + width*0.5, credit_apid_p95_cpu_1, width*.8,color='hotpink', label='APID_VM1',hatch='x',bottom=credit_apid_p95_cpu_2)

	rects3 = ax.bar(ind + width*0.5, credit_apid_p95_cpu_2, width*.8,color='palegreen', label='APID_VM2',hatch='-')
	rects4 = ax.bar(ind + width*1.5, credit_static_cpu_1, width*.8, color='dimgrey', label='STATIC_VM1',hatch='*',bottom=credit_static_cpu_2)

	rects4 = ax.bar(ind + width*1.5, credit_static_cpu_2, width*.8, color='lightgrey', label='STATIC_VM2',hatch='.')
	line = ax.plot([ind[0] - width*2,ind[-1] + width*2],[100,100],'k')
	# Add some text for labels, title and custom x-axis tick labels, etc.
	ax.set_ylabel('Average CPU Utilization Rate(%)')
	# ax.set_title('Scores by group and gender')
	ax.set_xticks(ind)
	ax.set_xticklabels(('Region 1\nVM1:Medium\nVM2:Medium', 'Region 2\nVM1:Medium\nVM2:Heavy', 'Region 3\nVM1:Heavy\nVM2:Heavy','Region 4\nVM1:Heavy\nVM2:Medium'),fontsize=9)
	ax.legend(loc='upper center', bbox_to_anchor=(0.5, 1.15),ncol=4, fancybox=True, shadow=False,fontsize=9)


	#MSE


	ind = np.arange(len(credit_aimd_inrange_1))  # the x locations for the groups
	width = 0.2  # the width of the bars
	patterns = ('*', '+', 'x', '\\', '*', 'o', 'O', '.')
	fig, ax = plt.subplots()
	rects1 = ax.bar(ind - width*1.5, rtds_aimd_mse_1, width*.8,color='b', label='AIMD_value_VM1',hatch='//')
	rects2 = ax.bar(ind - width*0.5, rtds_aimd_range_mse_1, width*.8,color='dodgerblue', label='AIMD_range_VM1',hatch='O')
	rects3 = ax.bar(ind + width*0.5, rtds_apid_p95_mse_1, width*.8,color='skyblue', label='APID_VM1',hatch='x')
	rects4 = ax.bar(ind + width*1.5, rtds_static_mse_1, width*.8, color='darkgrey', label='STATIC_VM1',hatch='*')

	# Add some text for labels, title and custom x-axis tick labels, etc.
	ax.set_ylabel("Mean Square Error (FPS^2)")
	# ax.set_title('Scores by group and gender')
	ax.set_xticks(ind)
	ax.set_xticklabels(('Region 1\nVM1:Medium\nVM2:Medium', 'Region 2\nVM1:Medium\nVM2:Heavy', 'Region 3\nVM1:Heavy\nVM2:Heavy','Region 4\nVM1:Heavy\nVM2:Medium'),fontsize=9)
	ax.legend()


	fig, ax = plt.subplots()
	rects1 = ax.bar(ind - width*1.5, rtds_aimd_mse_2, width*.8,color='b', label='AIMD_value_VM2',hatch='\\\\')
	rects2 = ax.bar(ind - width*0.5, rtds_aimd_range_mse_2, width*.8,color='dodgerblue', label='AIMD_range_VM2',hatch='o')
	rects3 = ax.bar(ind + width*0.5, rtds_apid_p95_mse_2, width*.8,color='skyblue', label='APID_VM2',hatch='-')
	rects4 = ax.bar(ind + width*1.5, rtds_static_mse_2, width*.8, color='darkgrey', label='STATIC_VM2',hatch='.')

	# Add some text for labels, title and custom x-axis tick labels, etc.
	ax.set_ylabel("Mean Square Error (FPS^2)")
	# ax.set_title('Scores by group and gender')
	ax.set_xticks(ind)
	ax.set_xticklabels(('Region 1\nVM1:Medium\nVM2:Medium', 'Region 2\nVM1:Medium\nVM2:Heavy', 'Region 3\nVM1:Heavy\nVM2:Heavy','Region 4\nVM1:Heavy\nVM2:Medium'),fontsize=9)
	ax.legend()



	fig, ax = plt.subplots()
	rects1 = ax.bar(ind - width*1.5, credit_aimd_mse_1, width*.8,color='g', label='AIMD_value_VM1',hatch='//')
	rects2 = ax.bar(ind - width*0.5, credit_aimd_range_mse_1, width*.8,color='limegreen', label='AIMD_range_VM1',hatch='O')
	rects3 = ax.bar(ind + width*0.5, credit_apid_p95_mse_1, width*.8,color='palegreen', label='APID_VM1',hatch='x')
	rects4 = ax.bar(ind + width*1.5, credit_static_mse_1, width*.8, color='darkgrey', label='STATIC_VM1',hatch='*')

	# Add some text for labels, title and custom x-axis tick labels, etc.
	ax.set_ylabel("Mean Square Error (FPS^2)")
	# ax.set_title('Scores by group and gender')
	ax.set_xticks(ind)
	ax.set_xticklabels(('Region 1\nVM1:Medium\nVM2:Medium', 'Region 2\nVM1:Medium\nVM2:Heavy', 'Region 3\nVM1:Heavy\nVM2:Heavy','Region 4\nVM1:Heavy\nVM2:Medium'),fontsize=9)
	ax.legend()


	fig, ax = plt.subplots()
	rects1 = ax.bar(ind - width*1.5, credit_aimd_mse_2, width*.8,color='g', label='AIMD_value_VM2',hatch='\\\\')
	rects2 = ax.bar(ind - width*0.5, credit_aimd_range_mse_2, width*.8,color='limegreen', label='AIMD_range_VM2',hatch='o')
	rects3 = ax.bar(ind + width*0.5, credit_apid_p95_mse_2, width*.8,color='palegreen', label='APID_VM2',hatch='-')
	rects4 = ax.bar(ind + width*1.5, credit_static_mse_2, width*.8, color='darkgrey', label='STATIC_VM2',hatch='.')

	# Add some text for labels, title and custom x-axis tick labels, etc.
	ax.set_ylabel("Mean Square Error (FPS^2)")
	# ax.set_title('Scores by group and gender')
	ax.set_xticks(ind)
	ax.set_xticklabels(('Region 1\nVM1:Medium\nVM2:Medium', 'Region 2\nVM1:Medium\nVM2:Heavy', 'Region 3\nVM1:Heavy\nVM2:Heavy','Region 4\nVM1:Heavy\nVM2:Medium'),fontsize=9)
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


