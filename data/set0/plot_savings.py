from os import listdir
from os.path import isfile, join
onlyfiles = [f for f in listdir('./') if isfile(join('./', f))]

files = [ f for f in onlyfiles if "savings_" in f]
print(files)




import matplotlib.pyplot as plt
import matplotlib.animation as animation
from matplotlib.widgets import Cursor
from matplotlib.font_manager import FontProperties
from matplotlib.widgets import CheckButtons

import time
for f in files:
    fig = plt.figure(figsize=(10, 7))
    ax1 = fig.add_subplot(2,1,1)
    ax2 = fig.add_subplot(2,1,2)
    buf = 1000
    show_frames=1
    show_anchors=1
    show_dummies=0
    show_ts=1
    font_per = [{'family': 'serif',
            'color':  'k',
            'size': 10,
            },{'family': 'serif',
            'color':  'k',
            # 'weight': 'bold',
            'size': 12,
            }]

    ax_rtxen = plt.axes([0, 0.91, 0.2, 0.12])
    ax_rtxen.text(0.06,0.42,'Average RT-Xen CPU\nutilization(%/sec):',fontdict=font_per[0])
    ax_rtxen_txt = ax_rtxen.text(0.1,0.01,'%.2f%%'%(0),fontdict=font_per[1])
    ax_rtxen.axis('off')

    ax_rtxen_inrange = plt.axes([0.2, 0.91, 0.2, 0.12])
    ax_rtxen_inrange.text(0.06,0.42,'Average RT-Xen CPU\nutilization(%/sec):',fontdict=font_per[0])
    ax_rtxen_inrange_txt = ax_rtxen_inrange.text(0.1,0.01,'%.2f%%'%(0),fontdict=font_per[1])
    ax_rtxen_inrange.axis('off')
 


    ax_xen = plt.axes([0.65, 0.91, 0.2, 0.12])
    ax_xen.text(0.08,0.42,'Average Credit CPU\nutilization(%/sec):',fontdict=font_per[0])
    ax_xen_txt = ax_xen.text(0.1,0.01,'%.2f%%'%(0),fontdict=font_per[1])
    ax_xen.axis('off')

    last_ts=[15,15]


    maxx=30000


    pullData = open(f,"r").read()
    minmax = open("minmax.txt","r").read()
    dataArray = pullData.split('\n')
    minmaxArray = minmax.split('\n')
    time_start=0
    time_end=0

    x = []
    hrs = []
    cpus = []
    anchor_xs = []
    anchors = []
    frame_xs = []
    frames = []
    dummy_x = []
    dummy_hrs = []
    ts_xs = []
    ts = []
    event_last_happened_at_cnt=[-1,-1]

    for i in range(2):
        x.append([])
        hrs.append([])        
        cpus.append([])
        anchor_xs.append([])
        anchors.append([])
        frame_xs.append([])
        frames.append([])
        dummy_x.append([])
        dummy_hrs.append([])        
        ts_xs.append([])
        ts.append([])




        # for j in range(buf):
        #     x[i].append(j)
        #     hrs[i].append(0)
        #     cpus[i].append(0)
    cnt=0
    maxhrs=0
    for eachLine in dataArray:
        if len(eachLine)>1:
            line = eachLine.split()
            if cnt==0:
                time_start = float(line[-1])
            time_end = float(line[-1])
            index=int(line[0])-1
            if len(line)==3+1:
                x[index].append(cnt)#float(line[-1])-time_start)
                hrs[index].append(float(line[1]))
                if float(line[1])>maxhrs:
                    maxhrs=float(line[1])
                cpus[index].append(float(line[2])/(1)*100)
            if len(line)==2+1:
                # print(line)
                anchor_xs[index].append(cnt)#float(line[-1])-time_start)
                anchors[index].append(int(line[1]))
                event_last_happened_at_cnt[index]=cnt

            if len(line)==4+1:
                frame_xs[index].append(cnt)#float(line[-1])-time_start)
                frames[index].append(int(line[1]))
                event_last_happened_at_cnt[index]=cnt

            if len(line)==5+1:
                dummy_x[index-2].append(cnt)#float(line[-1])-time_start)
                dummy_hrs[index-2].append(float(line[1]))
            if len(line)==6+1:
                ts_xs[index].append(cnt)#float(line[-1])-time_start)
                ts[index].append(int(line[1]))
                last_ts[index]=int(line[1])
                event_last_happened_at_cnt[index]=cnt
            # if len(line)==3:
            #     x[index].append(cnt)
            #     hrs[index].append(float(line[1]))
            #     if float(line[1])>maxhrs:
            #         maxhrs=float(line[1])
            #     cpus[index].append(float(line[2])/(1)*100)
            # if len(line)==2:
            #     anchor_xs[index].append(cnt)
            #     anchors[index].append(int(line[1]))
            #     event_last_happened_at_cnt[index]=cnt

            # if len(line)==4:
            #     frame_xs[index].append(cnt)
            #     frames[index].append(int(line[1]))
            #     event_last_happened_at_cnt[index]=cnt

            # if len(line)==5:
            #     dummy_x[index-2].append(cnt)
            #     dummy_hrs[index-2].append(float(line[1]))
            # if len(line)==6:
            #     ts_xs[index].append(cnt)
            #     ts[index].append(int(line[1]))
            #     last_ts[index]=int(line[1])
            #     event_last_happened_at_cnt[index]=cnt

            cnt+=1
    min_max = []
    for eachLine in minmaxArray:
        if len(eachLine)>1:
            line = eachLine.split()
            min_max.append(float(line[1]))

    ax1.clear()
    ax2.clear()
    sched=["RT-Xen","Credit"]
    colrs = ['blue','limegreen']
    for i in range(len(x)):
        ax1.scatter(x[i],hrs[i],s= ((1)%2)*6+5 ,label= sched[i] ,color=colrs[i])
        ax2.plot(x[i],cpus[i],color=colrs[i],lw=((i+1)%2)+3,label= sched[i] )
        # tmp=[]
        # for j in range(len(cpus[i])):
        #     tmp.append(100-cpus[i][j])
        # ax2.plot(x[i],tmp,color=dummy_colrs[i],lw=((i+1)%2)+3,label= sched[i] )
        # ax2.scatter(x[i],cpus[i],s= ((i+1)%2)*6+5,label= sched[i] ,color=colrs[i])
    dummy_colrs = ['cyan','lightgreen']
    dummy_sched=["Dummy\nRT-Xen","Dummy\nCredit"]

    if show_dummies:
        for i in range(len(dummy_x)):
            ax1.scatter(dummy_x[i],dummy_hrs[i],s= ((1)%2)*6+5 ,label= dummy_sched[i] ,color=dummy_colrs[i],marker='o')

    x_for_minmax = []
    miny = []
    maxy = []
    midy=[]
    total_x_len = len(x[0])+len(x[1])+len(dummy_x[0])+len(dummy_x[1])
    for i in range(total_x_len):
        x_for_minmax.append(i)
        miny.append(min_max[0])
        maxy.append(min_max[1])
        midy.append(min_max[0]/2+min_max[1]/2)


    # if time_start>0 and time_end>0 and len(miny)>1:
    #     ax1.plot([0,time_end-time_start],miny[0:2],'r')
    #     # ax1.plot([0,time_end-time_start],[(miny[0]+maxy[0])/2,(miny[0]+maxy[0])/2],'pink')
    #     ax1.plot([0,time_end-time_start],[(miny[0]+maxy[0])/2,(miny[0]+maxy[0])/2],'pink')
    #     ax1.plot([0,time_end-time_start],maxy[0:2],'r',label= 'Target\nFPS\nInterval')q
    ax1.plot(x_for_minmax,miny,'r')
    ax1.plot(x_for_minmax,midy,'pink')
    ax1.plot(x_for_minmax,maxy,'r',label= 'Target\nFPS\nRange')

    fontP = FontProperties()
    fontP.set_size('small')
    ax1.legend(bbox_to_anchor=(1.01, 1), loc=2, borderaxespad=0.,prop=fontP)
    # ax1.legend(loc='upper center', bbox_to_anchor=(0.5, 1.12),ncol=3, fancybox=True, shadow=True,prop=fontP)
    # ax2.legend(loc='upper center', bbox_to_anchor=(0.5, 1.1),ncol=3, fancybox=True, shadow=True,prop=fontP)
    ax2.legend(bbox_to_anchor=(1.01, 1), loc=2, borderaxespad=0.,prop=fontP)
    # fig.suptitle('RT-Xen vs Credit', fontsize=14, fontweight='bold')
    per = 0
    # try:
    #     rtxen_fps = hrs[0][-1]
    #     credit_fps = hrs[1][-1]
    #     per=(rtxen_fps-credit_fps)/credit_fps*100
   

    try:
        hrs_after_event_rtxen=0
        hrs_after_event_rtxen_cnt=0
        hrs_after_event_credit=0
        hrs_after_event_credit_cnt=0
        for ii,xx in enumerate(hrs[0]):
            if x[0][ii]>event_last_happened_at_cnt[0]:
                hrs_after_event_rtxen+=xx
                hrs_after_event_rtxen_cnt+=1
        for ii,xx in enumerate(hrs[1]):
            if x[1][ii]>event_last_happened_at_cnt[1]:
                hrs_after_event_credit+=xx
                hrs_after_event_credit_cnt+=1
        if hrs_after_event_rtxen_cnt > 0 and hrs_after_event_rtxen_cnt >0:
            rtxen_fps = hrs_after_event_rtxen/hrs_after_event_rtxen_cnt
            credit_fps = hrs_after_event_credit/hrs_after_event_credit_cnt
            per=(rtxen_fps-credit_fps)/credit_fps*100
    except:
        per=0

    area_under_curve_rtxen=0
    area_under_curve_xen=0
    if len(x[1])>0:
        for i in range(1,len(x[1])):
            area_under_curve_xen+=cpus[1][i-1]*(x[1][i]-x[1][i-1])
    if len(x[0])>0:
        for i in range(1,len(x[0])):
            area_under_curve_rtxen+=cpus[0][i-1]*(x[0][i]-x[0][i-1])


    if area_under_curve_xen>0:
        ax_xen_txt.set_text('%.2f%%'%(area_under_curve_xen/(x[1][-1]-x[1][0])))
    if area_under_curve_rtxen>0:
        ax_rtxen_txt.set_text('%.2f%%'%(area_under_curve_rtxen/(x[0][-1]-x[0][0])))

    # ax1.set_title('RT-Xen improved by: %.2f %%'%(per)+"\n",loc='right',fontdict=font_per[1])
    # ax1.set_title(r'$\frac{RT-Xen\'s improvement}{Percentage}$ = %.2f %%'%(per)+"\n",loc='right',fontsize=18)
    # ax1.set_title(r'$\frac{RT-Xen \quad FPS}{Credit \quad FPS }$ = %.2f %%'%(per)+"\n",loc='right',fontsize=18)
    # ax1.set_xlabel('Time\n \n')
    ax2.set_xlabel('Time(Heartbeat)')
    ax1.set_xlabel('Time(Heartbeat)')
    ax1.set_ylabel('Moving Average FPS(frames/sec) \n (Window Size = 12)')
    ax2.set_ylabel('Assigned CPU Utilization(%)')
    # ax2.set_ylim( 45, 105 )  
    ax2.set_ylim( -5, 105 )  
    ax=[ax1, ax2]
    font = [{'family': 'serif',
            'color':  'dodgerblue',
            'weight': 'bold',
            'size': 8,
            },{'family': 'serif',
            'color':  'forestgreen',
            'weight': 'bold',
            'size': 8,
            }]
    colrs = ['dodgerblue','forestgreen']

    if show_anchors:
        for i in range(len(anchor_xs)):
            for j in range(len(anchor_xs[i])):
                ax1.axvline(x=anchor_xs[i][j],color=colrs[i], linestyle='-')
                ax2.axvline(x=anchor_xs[i][j],color=colrs[i], linestyle='-')
                ymin,ymax=ax1.get_ylim()
                if anchors[i][j]==0:
                    ax1.text(anchor_xs[i][j],ymax,"50%",rotation=45,fontdict=font[i])
                elif anchors[i][j]==2:
                    ax1.text(anchor_xs[i][j],ymax,"100%",rotation=45,fontdict=font[i])
                elif anchors[i][j]==1:
                    ax1.text(anchor_xs[i][j],ymax,"Linear",rotation=45,fontdict=font[i])
                elif anchors[i][j]==3:
                    ax1.text(anchor_xs[i][j],ymax,"APID",rotation=45,fontdict=font[i])
                elif anchors[i][j]==4:
                    ax1.text(anchor_xs[i][j],ymax,"AIMD",rotation=45,fontdict=font[i])
    if show_frames:
        for i in range(len(frame_xs)):
            for j in range(len(frame_xs[i])):
                ax1.axvline(x=frame_xs[i][j],color=colrs[i], linestyle='--')
                ax2.axvline(x=frame_xs[i][j],color=colrs[i], linestyle='--')
                ax2.text(frame_xs[i][j],-10,"period: "+str(frames[i][j]),rotation=45,fontdict=font[i],horizontalalignment='right',verticalalignment='top')
    if show_ts:
        for i in range(len(ts_xs)):
            for j in range(len(ts_xs[i])):
                ax1.axvline(x=ts_xs[i][j],color=colrs[i], linestyle=':')
                ax2.axvline(x=ts_xs[i][j],color=colrs[i], linestyle=':')
                ax2.text(ts_xs[i][j],10,"ts: "+str(ts[i][j]),rotation=45,fontdict=font[i],horizontalalignment='right',verticalalignment='top')

plt.show()
