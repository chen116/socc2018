from os import listdir
from os.path import isfile, join
onlyfiles = [f for f in listdir('./') if isfile(join('./', f))]
# print(onlyfiles)

files = [ f for f in onlyfiles if "contention_vm_" in f]
print(files)


import numpy as np

import matplotlib.pyplot as plt
import matplotlib.animation as animation
from matplotlib.widgets import Cursor
from matplotlib.font_manager import FontProperties
from matplotlib.widgets import CheckButtons

import time
for f in files:

    print('\n')
    pullData = open(f,"r").read()
    minmax = open("minmax.txt","r").read()
    dataArray = pullData.split('\n')
    minmaxArray = minmax.split('\n')
    time_start=0
    time_end=0

    xs = []
    cpus_xs  =[]
    cpus = []
    hrs_mse = []
    mode_xs = []
    modes = []
    out_cpu = []


    out_hr_mse = []


    for i in range(2):
        xs.append([])
        cpus_xs.append([])    
        cpus.append([])
        hrs_mse.append([])

        mode_xs.append([])
        modes.append([])
        out_cpu.append([])
        out_hr_mse.append([])
        # for j in range(buf):
        #     x[i].append(j)
        #     hrs_mse[i].append(0)
        #     cpus[i].append(0)
    cnt=0
    maxhrs_mse=0
    for eachLine in dataArray:
        if len(eachLine)>1:
            line = eachLine.split()
            index=int(line[0])-1


            if len(line)==4+1:
                mode_xs[index].append(float(line[-1])-time_start)
                modes[index].append(int(line[1]))


                a=np.mean(np.asarray(cpus[0]))
                b=np.mean(np.asarray(cpus[1]))
                cpus[0]=[]
                cpus[1]=[]

                out_cpu[0].append(round(a,2))
                out_cpu[1].append(round(b,2))

                a=np.mean(np.asarray(hrs_mse[0]))
                b=np.mean(np.asarray(hrs_mse[1]))
                hrs_mse[0]=[]
                hrs_mse[1]=[]

                out_hr_mse[0].append(round(a,2))
                out_hr_mse[1].append(round(b,2))


            if len(line)==3+1:
                tmp_hr = float(line[1])
                se=0
                if tmp_hr > 11:
                    se = (tmp_hr-11)**2 
                elif tmp_hr < 9:
                    se = (9-tmp_hr)**2 
                hrs_mse[index].append(se)


            if len(line)==7+1:
                cpus_xs[index].append(float(line[-1])-time_start)
                cpus[index].append(round((float(line[1]))*100,2))
    a=np.mean(np.asarray(cpus[0]))
    b=np.mean(np.asarray(cpus[1]))
    out_cpu[0].append(round(a,2))
    out_cpu[1].append(round(b,2))
    var_name = f.split('.txt')[0].split('vm_')[1]
    # print(var_name+'_cpu_1 =',out_cpu[0])
    # print(var_name+'_cpu_2 =',out_cpu[1])

    a=np.mean(np.asarray(hrs_mse[0]))
    b=np.mean(np.asarray(hrs_mse[1]))
    out_hr_mse[0].append(round(a,2))
    out_hr_mse[1].append(round(b,2))
    var_name = f.split('.txt')[0].split('vm_')[1]
    print(var_name+'_mse_1 =',out_hr_mse[0])
    print(var_name+'_mse_2 =',out_hr_mse[1])
